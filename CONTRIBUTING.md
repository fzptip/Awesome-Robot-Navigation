# Contributing

Thanks for helping keep the list useful. Every change goes through `README.md`; the website is rebuilt from it automatically after each merge.

## Suggest a paper

The quickest way is the **Suggest a paper** issue form. A maintainer will add it.

## Add a paper yourself

1. Search the list (or the website) to make sure the paper is not there yet.
2. Add one line in this format:

   ```markdown
   - [Title of the Paper](https://doi.org/...), Surname et al., Venue Year.
   ```

   - Link the official version (DOI or proceedings page) when one exists, arXiv otherwise.
   - Authors: `Surname` for one author, `Surname and Surname` for two, `Surname et al.` for three or more.
   - Use the venue abbreviations already in the list: CVPR, ICRA, RA-L, IROS, ICCV, CoRL, RSS, ICLR, NeurIPS, ECCV, TRO, IJRR, JFR, T-MECH, TPAMI, Science Robotics. Preprints are `arXiv`.
   - Copy the title exactly, with plain `-` hyphens (not `‐` pasted from a publisher page).
3. List the paper in **every** section it belongs to, written identically each time. Most papers have a task (section 2), a method or capability (section 3), and often a platform (section 4) or a dataset or benchmark type (section 5).
4. Keep each section sorted: newest year first, then titles A to Z within a year.
5. Run the checker before opening a pull request:

   ```bash
   python3 scripts/build_site.py --check
   ```

   It reports entries it cannot parse, broken table-of-contents links, duplicates, ordering slips and inconsistent copies of the same paper. Pull requests run the same check automatically.

## Preview the website

```bash
python3 scripts/build_site.py --inline   # writes _site/index.html with the data embedded
open _site/index.html                     # or: python3 -m http.server -d _site
```

The page template lives in `site/index.html`; the build script only adds data to it.
