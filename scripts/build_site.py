#!/usr/bin/env python3
"""Build the Awesome Robot Navigation website from README.md.

README.md stays the single source of truth. This script parses it into
structured records (one per unique paper, listing every section it appears
in), injects them into site/index.html and writes the result to _site/.

    python3 scripts/build_site.py              # build _site/index.html + _site/papers.json
    python3 scripts/build_site.py --inline     # same, with the data embedded (open from disk)
    python3 scripts/build_site.py --check      # lint README.md only; exit 1 on errors
    python3 scripts/build_site.py --strict     # build, but fail on warnings too

papers.json is one JSON array with one typed record per line
("meta", "group", "section", "paper", "resource"), so it diffs well and other
tools can reuse it.

Only the Python standard library is used, so it runs anywhere Python 3.9+ does
(including a stock GitHub Actions runner).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------------------
# Configuration (edit here rather than in the parsing code)
# ---------------------------------------------------------------------------

# Subsections whose items are not research papers (books, courses, docs,
# competitions). Matched against the subsection title, case-insensitively.
RESOURCE_SECTION_PATTERNS = [
    r"tutorial|learning resource|course",
    r"competition|leaderboard",
]

# Venue spellings that mean the same thing. Left side -> canonical form.
# `--check` warns when both spellings are used in the README.
VENUE_ALIASES = {
    "Journal of Field Robotics": "JFR",
    "IEEE/ASME Transactions on Mechatronics": "T-MECH",
}

# Hostname -> label for the small link chips on the website.
LINK_TYPES = [
    ("arxiv.org", "arXiv"),
    ("doi.org", "DOI"),
    ("openaccess.thecvf.com", "CVF"),
    ("proceedings.mlr.press", "PMLR"),
    ("neurips.cc", "NeurIPS"),
    ("papers.nips.cc", "NeurIPS"),
    ("proceedings.iclr.cc", "ICLR"),
    ("openreview.net", "OpenReview"),
    ("roboticsproceedings.org", "RSS"),
    ("link.springer.com", "Springer"),
    ("aaai.org", "AAAI"),
]

DASHES = dict.fromkeys(map(ord, "‐‑‒–—−"), "-")

# ---------------------------------------------------------------------------
# Regular expressions for the README format
# ---------------------------------------------------------------------------

RE_H2 = re.compile(r"^##\s+(?P<num>\d+)\.\s+(?P<title>.+?)\s*$")
RE_H3 = re.compile(r"^###\s+(?P<num>\d+\.\d+)\s+(?P<title>.+?)\s*$")
RE_ANCHOR = re.compile(r'^<a id="(?P<id>[^"]+)"></a>\s*$')
RE_TOC = re.compile(r"^(?P<indent>\s*)- \[(?P<text>[^\]]+)\]\(#(?P<anchor>[^)]+)\)\s*$")
RE_ITEM = re.compile(r"^- \[(?P<title>.+)\]\((?P<url>https?://[^\s)]+)\)(?P<rest>.*)$")
# ", Authors, Venue Year."  (venue may itself contain commas, e.g. "MIT Press, 2nd ed.")
RE_PAPER_REST = re.compile(
    r"^,\s*(?P<authors>[^,]+?),\s*(?P<venue>.+?),?\s+(?P<year>(?:19|20)\d{2})\.?\s*$"
)
# ", Organisation. Free-text note."
RE_RESOURCE_REST = re.compile(r"^,\s*(?P<org>.+?)\.\s+(?P<note>.+?)\.?\s*$")


class Report:
    """Collects lint findings so --check can print them in one place."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, line: int | None, msg: str) -> None:
        self.errors.append(f"README.md:{line}: {msg}" if line else msg)

    def warn(self, line: int | None, msg: str) -> None:
        self.warnings.append(f"README.md:{line}: {msg}" if line else msg)


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def title_key(title: str) -> str:
    """Normalised title used to detect the same paper listed twice."""
    t = unicodedata.normalize("NFKD", title.translate(DASHES))
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", " ", t).strip()


def link_type(url: str) -> str:
    host = urlparse(url).netloc.lower()
    for needle, label in LINK_TYPES:
        if host == needle or host.endswith("." + needle) or needle in host:
            return label
    return "PDF" if url.lower().split("?")[0].endswith(".pdf") else "Web"


def canonical_venue(venue: str) -> str:
    return VENUE_ALIASES.get(venue, venue)


def resource_kind(section_title: str, title: str, note: str) -> str:
    if re.search(r"competition|leaderboard", section_title, re.I):
        return "Competition"
    text = f"{title} {note}".lower()
    if "course" in text:
        return "Course"
    if re.search(r"documentation|tutorials|user guide|getting started|docs", text):
        return "Documentation"
    return "Book"


# ---------------------------------------------------------------------------
# Parsing
# ---------------------------------------------------------------------------


def parse_readme(text: str, report: Report) -> dict:
    lines = text.splitlines()
    groups: list[dict] = []
    sections: list[dict] = []
    entries: list[dict] = []
    toc: list[tuple[int, str, str]] = []
    anchors: dict[str, int] = {}

    group = section = None
    pending_anchor: tuple[str, int] | None = None
    in_toc = False

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip()

        if line.strip().lower().strip("*#: ") in ("table of contents", "contents"):
            in_toc = True
            continue

        m = RE_ANCHOR.match(line)
        if m:
            in_toc = False
            anchors[m["id"]] = i
            pending_anchor = (m["id"], i)
            prev = lines[i - 2].strip() if i >= 2 else ""
            if prev:
                report.warn(i, f'missing blank line before anchor "{m["id"]}" '
                               "(it renders inside the previous list item)")
            continue

        if in_toc:
            t = RE_TOC.match(line)
            if t:
                toc.append((i, t["text"], t["anchor"]))
            continue

        m = RE_H2.match(line)
        if m:
            group = {
                "id": m["num"],
                "title": m["title"],
                "slug": slugify(m["title"]),
                "anchor": pending_anchor[0] if pending_anchor else None,
                "sections": [],
                "line": i,
            }
            if not pending_anchor:
                report.error(i, f'heading "{line}" has no <a id> anchor above it')
            groups.append(group)
            section, pending_anchor = None, None
            continue

        m = RE_H3.match(line)
        if m:
            title = m["title"]
            kind = "resources" if any(
                re.search(p, title, re.I) for p in RESOURCE_SECTION_PATTERNS
            ) else "papers"
            section = {
                "id": m["num"],
                "title": title,
                "slug": slugify(title),
                "group": group["id"] if group else None,
                "anchor": pending_anchor[0] if pending_anchor else None,
                "description": "",
                "kind": kind,
                "line": i,
            }
            if not pending_anchor:
                report.error(i, f'heading "{line}" has no <a id> anchor above it')
            if group and not m["num"].startswith(group["id"] + "."):
                report.warn(i, f"subsection {m['num']} sits under section {group['id']}")
            sections.append(section)
            if group:
                group["sections"].append(section["id"])
            pending_anchor = None
            continue

        if section is None:
            continue

        if line.startswith("- ["):
            m = RE_ITEM.match(line)
            if not m:
                report.error(i, f"could not parse list item: {line[:90]}")
                continue
            entry = {
                "title": m["title"].strip(),
                "url": m["url"],
                "section": section["id"],
                "line": i,
            }
            rest = m["rest"].strip()
            pm = RE_PAPER_REST.match(rest)
            rm = RE_RESOURCE_REST.match(rest)
            if section["kind"] == "papers":
                if not pm:
                    report.error(i, f'expected "[Title](url), Authors, Venue Year." '
                                    f"but got: {line[:90]}")
                    continue
                entry.update(authors=pm["authors"].strip(), venue=pm["venue"].strip(),
                             year=int(pm["year"]))
            else:
                if pm:
                    entry.update(org=pm["authors"].strip(), venue=pm["venue"].strip(),
                                 year=int(pm["year"]), note="")
                elif rm:
                    entry.update(org=rm["org"].strip(), venue="", year=None,
                                 note=rm["note"].strip())
                else:
                    report.error(i, f"could not parse resource: {line[:90]}")
                    continue
                yr = re.search(r"\b(19|20)\d{2}\b", f'{entry["title"]} {entry["note"]}')
                if entry["year"] is None and yr:
                    entry["year"] = int(yr.group(0))
                entry["kind"] = resource_kind(section["title"], entry["title"], entry["note"])
            entries.append(entry)
            continue

        stripped = line.strip()
        if stripped and not section["description"] and not entries_in(section, entries):
            section["description"] = stripped

    return {"groups": groups, "sections": sections, "entries": entries,
            "toc": toc, "anchors": anchors, "lines": lines}


def entries_in(section: dict, entries: list[dict]) -> bool:
    return bool(entries) and entries[-1]["section"] == section["id"]


# ---------------------------------------------------------------------------
# Checks
# ---------------------------------------------------------------------------


def lint(parsed: dict, report: Report) -> None:
    groups, sections, entries = parsed["groups"], parsed["sections"], parsed["entries"]
    anchors, toc = parsed["anchors"], parsed["toc"]

    # Table of contents <-> headings
    toc_anchors = {a for _, _, a in toc}
    for line, text, anchor in toc:
        if anchor not in anchors:
            report.error(line, f'TOC link "{text}" points to missing anchor #{anchor}')
    for s in groups + sections:
        if s["anchor"] and s["anchor"] not in toc_anchors:
            report.warn(s["line"], f'"{s["id"]} {s["title"]}" is missing from the TOC')

    # Numbering gaps (e.g. 1.3 with no 1.1)
    for g in groups:
        nums = [int(sid.split(".")[1]) for sid in g["sections"]]
        expected = list(range(1, len(nums) + 1))
        if nums != expected:
            report.warn(g["line"], f'section {g["id"]} numbers its subsections '
                                   f'{", ".join(g["id"] + "." + str(n) for n in nums)} '
                                   f"(expected {g['id']}.1 ... {g['id']}.{len(nums)})")

    by_section: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        by_section[e["section"]].append(e)

    for s in sections:
        items = by_section.get(s["id"], [])
        if not items:
            report.warn(s["line"], f'section {s["id"]} {s["title"]} is empty')
        if not s["description"]:
            report.warn(s["line"], f'section {s["id"]} has no description paragraph')

        # Duplicates inside one section
        seen: dict[str, int] = {}
        for e in items:
            k = title_key(e["title"])
            if k in seen:
                report.error(e["line"], f'"{e["title"]}" is listed twice in {s["id"]} '
                                        f'(also line {seen[k]})')
            seen[k] = e["line"]

        if s["kind"] != "papers":
            continue
        # Ordering: newest first, then alphabetical within a year
        for a, b in zip(items, items[1:]):
            if b["year"] > a["year"]:
                report.warn(b["line"], f'{s["id"]}: {b["year"]} entry after {a["year"]} '
                                       f'entry (list is newest-first): "{b["title"][:60]}"')
            elif b["year"] == a["year"] and title_key(b["title"]) < title_key(a["title"]):
                report.warn(b["line"], f'{s["id"]}: not alphabetical within {a["year"]}: '
                                       f'"{b["title"][:50]}" after "{a["title"][:50]}"')

    # The same paper listed in several sections should be written identically
    groups_by_key: dict[str, list[dict]] = defaultdict(list)
    for e in entries:
        if "authors" in e:
            groups_by_key[title_key(e["title"])].append(e)
    for dupes in groups_by_key.values():
        if len(dupes) < 2:
            continue
        first = dupes[0]
        for other in dupes[1:]:
            diffs = [f for f in ("title", "url", "authors", "venue", "year")
                     if other[f] != first[f]]
            if diffs:
                report.warn(other["line"],
                            f'"{first["title"][:55]}" differs from line {first["line"]} in: '
                            + ", ".join(diffs))

    # Venue spelling consistency
    venues = Counter(e.get("venue", "") for e in entries if "authors" in e)
    for alias, canon in VENUE_ALIASES.items():
        if venues[alias] and venues[canon]:
            report.warn(None, f'venue written both as "{canon}" ({venues[canon]}x) and '
                              f'"{alias}" ({venues[alias]}x)')

    # Typographic dashes make search miss matches ("Point-LIO" vs "Point‐LIO")
    for e in entries:
        if e["title"] != e["title"].translate(DASHES):
            report.warn(e["line"], f'non-ASCII hyphen in title: "{e["title"][:60]}"')


# ---------------------------------------------------------------------------
# Building the dataset
# ---------------------------------------------------------------------------


def git(repo: Path, *args: str) -> str | None:
    try:
        return subprocess.run(["git", "-C", str(repo), *args], check=True,
                              capture_output=True, text=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return None


def line_dates(readme: Path) -> dict[int, str]:
    """Map README line number -> date the line was last changed (via git blame).

    Needs full history (actions/checkout with fetch-depth: 0); skipped otherwise.
    """
    repo = readme.parent
    if (git(repo, "rev-parse", "--is-shallow-repository") or "").strip() != "false":
        return {}
    if git(repo, "diff", "--quiet", "--", readme.name) is None:
        return {}  # uncommitted edits: blame line numbers would not match
    out = git(repo, "blame", "--line-porcelain", "--", readme.name)
    if not out:
        return {}
    dates, current = {}, None
    for row in out.splitlines():
        parts = row.split()
        if len(parts) >= 3 and re.fullmatch(r"[0-9a-f]{40}", parts[0]):
            current = int(parts[2])
        elif row.startswith("author-time ") and current is not None:
            ts = int(row.split()[1])
            dates[current] = dt.datetime.fromtimestamp(ts, dt.timezone.utc).date().isoformat()
    return dates


def build_dataset(parsed: dict, dates: dict[int, str], repo: Path) -> dict:
    papers: dict[str, dict] = {}
    resources: list[dict] = []

    for e in parsed["entries"]:
        added = dates.get(e["line"])
        if "authors" not in e:
            resources.append({
                "title": e["title"], "url": e["url"], "org": e["org"],
                "venue": e["venue"], "year": e["year"], "note": e["note"],
                "kind": e["kind"], "section": e["section"], "added": added,
            })
            continue
        key = title_key(e["title"])
        p = papers.get(key)
        if p is None:
            p = papers[key] = {
                "title": e["title"], "authors": e["authors"],
                "venue": canonical_venue(e["venue"]), "year": e["year"],
                "links": [], "sections": [], "added": added,
            }
        if e["section"] not in p["sections"]:
            p["sections"].append(e["section"])
        if all(l["url"] != e["url"] for l in p["links"]):
            p["links"].append({"url": e["url"], "type": link_type(e["url"])})
        if added and (not p["added"] or added < p["added"]):
            p["added"] = added

    paper_list = sorted(papers.values(), key=lambda p: (-p["year"], title_key(p["title"])))
    for n, p in enumerate(paper_list, start=1):
        p["id"] = f"p{n}"

    counts = Counter(s for p in paper_list for s in p["sections"])
    counts.update(r["section"] for r in resources)
    sections = [{
        "id": s["id"], "title": s["title"], "slug": s["slug"], "group": s["group"],
        "anchor": s["anchor"], "description": s["description"], "kind": s["kind"],
        "count": counts.get(s["id"], 0),
    } for s in parsed["sections"]]
    groups = [{"id": g["id"], "title": g["title"], "slug": g["slug"],
               "anchor": g["anchor"], "sections": g["sections"]} for g in parsed["groups"]]

    commit = (git(repo, "rev-parse", "HEAD") or "").strip() or None
    commit_date = (git(repo, "log", "-1", "--format=%cs") or "").strip() or None
    return {
        "generated": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),
        "commit": commit,
        "updated": commit_date,
        "stats": {
            "papers": len(paper_list),
            "listings": sum(1 for e in parsed["entries"] if "authors" in e),
            "resources": len(resources),
        },
        "groups": groups,
        "sections": sections,
        "papers": paper_list,
        "resources": resources,
    }


def guess_repo(repo_dir: Path) -> str | None:
    """owner/name from $GITHUB_REPOSITORY (set in Actions) or the origin remote."""
    import os
    if os.environ.get("GITHUB_REPOSITORY"):
        return os.environ["GITHUB_REPOSITORY"]
    url = (git(repo_dir, "remote", "get-url", "origin") or "").strip()
    m = re.search(r"github\.com[:/]([^/]+/[^/]+?)(?:\.git)?$", url)
    return m.group(1) if m else None


def to_rows(data: dict, repo: str | None) -> list[dict]:
    """Flatten the dataset into typed records (one JSON object per line on disk)."""
    meta = {"type": "meta", "repo": repo, "generated": data["generated"],
            "commit": data["commit"], "updated": data["updated"], **data["stats"]}
    return ([meta]
            + [{"type": "group", **g} for g in data["groups"]]
            + [{"type": "section", **s} for s in data["sections"]]
            + [{"type": "paper", **p} for p in data["papers"]]
            + [{"type": "resource", **r} for r in data["resources"]])


def rows_json(rows: list[dict]) -> str:
    lines = (json.dumps(r, ensure_ascii=False, separators=(",", ":")) for r in rows)
    return "[\n" + ",\n".join(lines) + "\n]\n"


def render(template: str, rows: list[dict] | None) -> str:
    """Copy the template; with rows, embed them so the page works from file://."""
    marker = "/*__DATA__*/null"
    if marker not in template:
        sys.exit(f"template is missing the {marker!r} placeholder")
    if rows is None:
        return template
    payload = json.dumps(rows, ensure_ascii=False, separators=(",", ":"))
    return template.replace(marker, payload.replace("</", "<\\/"), 1)


# ---------------------------------------------------------------------------


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--readme", type=Path, default=ROOT / "README.md")
    ap.add_argument("--template", type=Path, default=ROOT / "site" / "index.html")
    ap.add_argument("--out", type=Path, default=ROOT / "_site")
    ap.add_argument("--repo", help="GitHub owner/name for links (default: from git)")
    ap.add_argument("--inline", action="store_true",
                    help="embed the data in index.html so it opens straight from disk")
    ap.add_argument("--check", action="store_true", help="lint README.md and exit")
    ap.add_argument("--strict", action="store_true", help="treat warnings as errors")
    ap.add_argument("--quiet", action="store_true", help="only print the summary")
    args = ap.parse_args(argv)

    report = Report()
    parsed = parse_readme(args.readme.read_text(encoding="utf-8"), report)
    lint(parsed, report)

    if not args.quiet:
        for msg in report.errors:
            print(f"error: {msg}")
        for msg in report.warnings:
            print(f"warning: {msg}")
    print(f"{len(parsed['entries'])} entries in {len(parsed['sections'])} sections: "
          f"{len(report.errors)} errors, {len(report.warnings)} warnings")

    failed = bool(report.errors) or (args.strict and bool(report.warnings))
    if args.check:
        return 1 if failed else 0
    if report.errors:
        print("not building: fix the errors above first")
        return 1

    readme = args.readme.resolve()
    data = build_dataset(parsed, line_dates(readme), readme.parent)
    rows = to_rows(data, args.repo or guess_repo(readme.parent))
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "papers.json").write_text(rows_json(rows), encoding="utf-8")
    (args.out / "index.html").write_text(
        render(args.template.read_text(encoding="utf-8"), rows if args.inline else None),
        encoding="utf-8")
    (args.out / ".nojekyll").write_text("", encoding="utf-8")
    print(f"built {args.out}/index.html: {data['stats']['papers']} unique papers, "
          f"{data['stats']['resources']} resources")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
