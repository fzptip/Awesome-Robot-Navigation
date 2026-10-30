# Awesome Robot Navigation [![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Table of Contents**

- [1. Overview and Surveys](#section-1)
  - [1.3 Surveys and Reviews](#section-1-3)
  - [1.4 Tutorials and Learning Resources](#section-1-4)
- [2. Navigation Tasks](#section-2)
  - [2.1 Geometric Goal Navigation](#section-2-1)
  - [2.2 Visual Goal Navigation](#section-2-2)
  - [2.3 Semantic Goal Navigation](#section-2-3)
  - [2.4 Language-Guided Navigation](#section-2-4)
  - [2.5 Autonomous Exploration](#section-2-5)
  - [2.6 Coverage and Inspection](#section-2-6)
  - [2.7 Moving Target Following](#section-2-7)
- [3. Navigation Methods and Core Capabilities](#section-3)
  - [3.1 Foundation Model-Based Navigation](#section-3-1)
  - [3.2 World Model-Based Navigation](#section-3-2)
  - [3.3 End-to-End Navigation and Policy Learning](#section-3-3)
  - [3.4 Perception, Representation, and Memory](#section-3-4)
  - [3.5 Odometry and State Estimation](#section-3-5)
  - [3.6 Localization and Mapping](#section-3-6)
  - [3.7 Path Planning and Decision Making](#section-3-7)
- [4. Robot Platforms](#section-4)
  - [4.1 Unmanned Aerial Vehicles](#section-4-1)
  - [4.2 Wheeled Robots](#section-4-2)
  - [4.3 Humanoid Robots](#section-4-3)
  - [4.4 Quadruped Robots](#section-4-4)
  - [4.5 Underwater Robots](#section-4-5)
  - [4.6 Other and Hybrid Platforms](#section-4-6)
- [5. Datasets and Evaluation Benchmarks](#section-5)
  - [5.1 Odometry, Localization, and Mapping Datasets](#section-5-1)
  - [5.2 Navigation Task Datasets and Benchmarks](#section-5-2)
  - [5.3 Real-Robot and Cross-Platform Data](#section-5-3)
  - [5.4 Evaluation Metrics and Experimental Protocols](#section-5-4)
  - [5.5 Competitions and Leaderboards](#section-5-5)

<a id="section-1"></a>

## 1. Overview and Surveys

<a id="section-1-3"></a>

### 1.3 Surveys and Reviews

Surveys of robot navigation tasks and methods, covering embodied and language-guided navigation, foundation models, world models, exploration, SLAM, perception, planning, and social navigation.

- [World model for robot learning: A comprehensive survey](https://doi.org/10.1177/02783649261488980), Hou et al., IJRR 2026.

- [Robot Navigation via Foundation Language Models: A Review](https://doi.org/10.1145/3802539), Pan et al., ACM Computing Surveys 2026.

- [Multi-Robot System for Cooperative Exploration in Unknown Environments: A Survey](https://arxiv.org/abs/2503.07278), Wang et al., arXiv 2025.

- [A Survey of Object Goal Navigation](https://doi.org/10.1109/tase.2024.3378010), Sun et al., TASE 2025.

- [Vision-and-Language Navigation Today and Tomorrow: A Survey in the Era of Foundation Models](https://arxiv.org/abs/2407.07035), Zhang et al., TMLR 2024.

- [Embodied navigation with multi-modal information: A survey from tasks to methodology](https://doi.org/10.1016/j.inffus.2024.102532), Wu et al., Information Fusion 2024.

- [A Comprehensive Review of Mobile Robot Navigation Using Deep Reinforcement Learning Algorithms in Crowded Environments](https://doi.org/10.1007/s10846-024-02198-w), Le et al., Journal of Intelligent & Robotic Systems 2024.

- [Bridging Requirements, Planning, and Evaluation: A Review of Social Robot Navigation](https://doi.org/10.3390/s24092794), Karwowski et al., Sensors 2024.

- [A Survey on Active Simultaneous Localization and Mapping: State of the Art and New Frontiers](https://doi.org/10.1109/tro.2023.3248510), Placed et al., TRO 2023.

- [Event-Based Vision: A Survey](https://doi.org/10.1109/tpami.2020.3008413), Gallego et al., TPAMI 2022.

- [Survey of UAV motion planning](https://doi.org/10.1049/iet-csr.2020.0004), Quan et al., IET Cyber-Systems and Robotics 2020.

- [Past, Present, and Future of Simultaneous Localization and Mapping: Toward the Robust-Perception Age](https://doi.org/10.1109/tro.2016.2624754), Cadena et al., TRO 2016.

- [Visual Place Recognition: A Survey](https://doi.org/10.1109/tro.2015.2496823), Lowry et al., TRO 2016.

- [Sampling-Based Robot Motion Planning: A Review](https://doi.org/10.1109/access.2014.2302442), Elbanhawi et al., IEEE Access 2014.

- [A survey on coverage path planning for robotics](https://doi.org/10.1016/j.robot.2013.09.004), Galceran et al., Robotics and Autonomous Systems 2013.

<a id="section-1-4"></a>

### 1.4 Tutorials and Learning Resources

Textbooks, tutorial monographs, university courses, and official documentation for mobile robotics, state estimation, planning, reinforcement learning, simulation, and robot deployment.

- [State Estimation for Robotics](https://www.cambridge.org/core/books/state-estimation-for-robotics/00E53274A2F1E6CC1A55CA5C3D1C9718), Barfoot, Cambridge University Press, 2nd ed. 2024.

- [Reinforcement Learning: An Introduction](https://mitpress.mit.edu/9780262039246/reinforcement-learning/), Sutton and Barto, MIT Press, 2nd ed. 2018.

- [Factor Graphs for Robot Perception](https://doi.org/10.1561/2300000043), Dellaert et al., Foundations and Trends in Robotics 2017.

- [Modern Robotics: Mechanics, Planning, and Control](https://modernrobotics.northwestern.edu/), Lynch and Park, Cambridge University Press 2017.

- [Introduction to Autonomous Mobile Robots](https://mitpress.mit.edu/9780262015356/introduction-to-autonomous-mobile-robots/), Siegwart et al., MIT Press, 2nd ed. 2011.

- [Planning Algorithms](https://lavalle.pl/planning/), LaValle, Cambridge University Press 2006.

- [Probabilistic Robotics](https://mitpress.mit.edu/9780262303804/probabilistic-robotics/), Thrun et al., MIT Press 2005.

- [Autonomous Mobile Robots](https://asl.ethz.ch/education/lectures/autonomous_mobile_robots.html), ETH Zurich Autonomous Systems Lab. Official course materials.

- [Underactuated Robotics](https://underactuated.mit.edu/), Tedrake, MIT. Official online textbook and course notes.

- [Deep Reinforcement Learning (CS185/285)](https://rail.eecs.berkeley.edu/deeprlcourse/), UC Berkeley. Official course materials.

- [Habitat Lab Documentation](https://aihabitat.org/docs/habitat-lab/), Habitat Team. Official documentation and tutorials.

- [ROS 2 Tutorials](https://docs.ros.org/en/rolling/Tutorials.html), ROS 2 Project. Official tutorials.

- [Nav2 Documentation](https://docs.nav2.org/), Nav2 Team. Official documentation and tutorials.

- [Getting Started with Gazebo](https://gazebosim.org/docs/latest/getstarted/), Gazebo Project. Official documentation and tutorials.

- [PX4 Autopilot User Guide](https://docs.px4.io/main/en/), PX4 Project. Official documentation and tutorials.

<a id="section-2"></a>

## 2. Navigation Tasks

<a id="section-2-1"></a>

### 2.1 Geometric Goal Navigation

Navigation to target coordinates, poses, or waypoint sequences, including settings with perfect localization, no ground-truth localization, sensor noise, and real robots.

- [Seeing Through Uncertainty: Free-Energy-Inspired Real-Time Adaptation for Robust Visual Navigation](https://arxiv.org/abs/2403.01977), Piriyajitakonkij et al., RA-L 2026.

- [Learning Decentralized Multi-Robot PointGoal Navigation](https://doi.org/10.1109/lra.2025.3550798), Soualhi et al., RA-L 2025.

- [MPVO: Motion-Prior based Visual Odometry for PointGoal Navigation](https://arxiv.org/abs/2411.04796), Paul et al., ECCV Workshops 2024.

- [Emergence of Maps in the Memories of Blind Navigation Agents](https://arxiv.org/abs/2301.13261), Wijmans et al., ICLR 2023.

- [Unsupervised Visual Odometry and Action Integration for PointGoal Navigation in Indoor Environment](https://arxiv.org/abs/2210.00413), Cao et al., TCSVT 2023.

- [How to Train PointGoal Navigation Agents on a (Sample and Compute) Budget](https://arxiv.org/abs/2012.06117), Wijmans et al., AAMAS (Extended Abstract) 2022.

- [Is Mapping Necessary for Realistic PointGoal Navigation?](https://arxiv.org/abs/2206.00997), Partsey et al., CVPR 2022.

- [Safe-Nav: learning to prevent PointGoal navigation failure in unknown environments](https://link.springer.com/article/10.1007/s40747-022-00648-2), Jin et al., Complex & Intelligent Systems 2022.

- [Out of the Box: Embodied Navigation in the Real World](https://arxiv.org/abs/2105.05873), Bigazzi et al., CAIP 2021.

- [Realistic PointGoal Navigation via Auxiliary Losses and Information Bottleneck](https://arxiv.org/abs/2109.08677), Grande et al., arXiv 2021.

- [The Surprising Effectiveness of Visual Odometry Techniques for Embodied PointGoal Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Zhao_The_Surprising_Effectiveness_of_Visual_Odometry_Techniques_for_Embodied_PointGoal_ICCV_2021_paper.html), Zhao et al., ICCV 2021.

- [Auxiliary Tasks Speed Up Learning PointGoal Navigation](https://arxiv.org/abs/2007.04561), Ye et al., CoRL 2020.

- [DD-PPO: Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames](https://arxiv.org/abs/1911.00357), Wijmans et al., ICLR 2020.

- [Integrating Egocentric Localization for More Realistic Point-Goal Navigation Agents](https://arxiv.org/abs/2009.03231), Datta et al., CoRL 2020.

- [Learning to Explore using Active Neural SLAM](https://arxiv.org/abs/2004.05155), Chaplot et al., ICLR 2020.

- [Learning to Move with Affordance Maps](https://arxiv.org/abs/2001.02364), Qi et al., ICLR 2020.

<a id="section-2-2"></a>

### 2.2 Visual Goal Navigation

Goals specified by reference images, panoramic images, or images of specific object instances, covering image-goal, instance-image-goal, and multimodal navigation.

- [AnyImageNav: Any-View Geometry for Precise Last-Meter Image-Goal Navigation](https://arxiv.org/abs/2604.05351), Deng et al., arXiv 2026.

- [FeudalNav: A Simple Framework for Visual Navigation](https://arxiv.org/abs/2602.06974), Johnson et al., arXiv 2026.

- [GeniNav: Generative Model Driven Image-Goal Navigation via Imagination-Guided Consistency Flow Matching](https://openaccess.thecvf.com/content/CVPR2026/html/Chen_GeniNav_Generative_Model_Driven_Image-Goal_Navigation_via_Imagination-Guided_Consistency_Flow_CVPR_2026_paper.html), Chen et al., CVPR 2026.

- [Hierarchical Scoring with 3D Gaussian Splatting for Instance Image-Goal Navigation](https://arxiv.org/abs/2506.07338), Deng et al., RA-L 2026.

- [RSRNav: Reasoning Spatial Relationship for Image-Goal Navigation](https://arxiv.org/abs/2504.17991), Qin et al., TCSVT 2026.

- [Think before Go: Hierarchical Reasoning for Image-goal Navigation](https://arxiv.org/abs/2604.17407), Li et al., ACL 2026.

- [What does really matter in image goal navigation?](https://arxiv.org/abs/2507.01667), Monaci et al., 3DV 2026.

- [GaussNav: Gaussian Splatting for Visual Navigation](https://arxiv.org/abs/2403.11625), Lei et al., TPAMI 2025.

- [IGL-Nav: Incremental 3D Gaussian Localization for Image-goal Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Guo_IGL-Nav_Incremental_3D_Gaussian_Localization_for_Image-goal_Navigation_ICCV_2025_paper.html), Guo et al., ICCV 2025.

- [Image-Goal Navigation Using Refined Feature Guidance and Scene Graph Enhancement](https://arxiv.org/abs/2503.10986), Feng et al., IROS 2025.

- [NavigateDiff: Visual Predictors are Zero-Shot Navigation Assistants](https://arxiv.org/abs/2502.13894), Qin et al., ICRA 2025.

- [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html), Bar et al., CVPR 2025.

- [PIG-Nav: Key Insights for Pretrained Image Goal Navigation Models](https://arxiv.org/abs/2507.17220), Wan et al., arXiv 2025.

- [RANa: Retrieval-Augmented Navigation](https://arxiv.org/abs/2504.03524), Monaci et al., TMLR 2025.

- [REGNav: Room Expert Guided Image-Goal Navigation](https://arxiv.org/abs/2502.10785), Li et al., AAAI 2025.

- [End-to-End (Instance)-Image Goal Navigation through Correspondence as an Emergent Phenomenon](https://arxiv.org/abs/2309.16634), Bono et al., ICLR 2024.

- [GOAT: GO to Any Thing](https://arxiv.org/abs/2311.06430), Chang et al., RSS 2024.

- [Instance-aware Exploration-Verification-Exploitation for Instance ImageGoal Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Lei_Instance-aware_Exploration-Verification-Exploitation_for_Instance_ImageGoal_Navigation_CVPR_2024_paper.html), Lei et al., CVPR 2024.

- [MemoNav: Working Memory Model for Visual Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MemoNav_Working_Memory_Model_for_Visual_Navigation_CVPR_2024_paper.html), Li et al., CVPR 2024.

- [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896), Sridhar et al., ICRA 2024.

- [FGPrompt: Fine-grained Goal Prompting for Image-goal Navigation](https://arxiv.org/abs/2310.07473), Sun et al., NeurIPS 2023.

- [GNM: A General Navigation Model to Drive Any Robot](https://arxiv.org/abs/2210.03370), Shah et al., ICRA 2023.

- [Navigating to Objects Specified by Images](https://openaccess.thecvf.com/content/ICCV2023/html/Krantz_Navigating_to_Objects_Specified_by_Images_ICCV_2023_paper.html), Krantz et al., ICCV 2023.

- [Offline Visual Representation Learning for Embodied Navigation](https://arxiv.org/abs/2204.13226), Yadav et al., ICLR Workshops 2023.

- [OVRL-V2: A simple state-of-art baseline for ImageNav and ObjectNav](https://arxiv.org/abs/2303.07798), Yadav et al., arXiv 2023.

- [ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846), Shah et al., CoRL 2023.

- [Image-Goal Navigation in Complex Environments via Modular Learning](https://arxiv.org/abs/2108.06105), Wu et al., RA-L 2022.

- [Last-Mile Embodied Visual Navigation](https://arxiv.org/abs/2211.11746), Wasserman et al., CoRL 2022.

- [Memory-Augmented Reinforcement Learning for Image-Goal Navigation](https://arxiv.org/abs/2101.05181), Mezghani et al., IROS 2022.

- [Topological Semantic Graph Memory for Image-Goal Navigation](https://arxiv.org/abs/2209.08274), Kim et al., CoRL 2022.

- [No RL, No Simulation: Learning to Navigate without Navigating](https://arxiv.org/abs/2110.09470), Hahn et al., NeurIPS 2021.

- [Pose Invariant Topological Memory for Visual Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Taniguchi_Pose_Invariant_Topological_Memory_for_Visual_Navigation_ICCV_2021_paper.html), Taniguchi et al., ICCV 2021.

- [Visual Graph Memory With Unsupervised Representation for Visual Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Kwon_Visual_Graph_Memory_With_Unsupervised_Representation_for_Visual_Navigation_ICCV_2021_paper.html), Kwon et al., ICCV 2021.

- [Learning Your Way Without Map or Compass: Panoramic Target Driven Visual Navigation](https://arxiv.org/abs/1909.09295), Watkins-Valls et al., IROS 2020.

- [Neural Topological SLAM for Visual Navigation](https://openaccess.thecvf.com/content_CVPR_2020/html/Chaplot_Neural_Topological_SLAM_for_Visual_Navigation_CVPR_2020_paper.html), Chaplot et al., CVPR 2020.

- [Semi-parametric Topological Memory for Navigation](https://arxiv.org/abs/1803.00653), Savinov et al., ICLR 2018.

- [Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning](https://arxiv.org/abs/1609.05143), Zhu et al., ICRA 2017.

<a id="section-2-3"></a>

### 2.3 Semantic Goal Navigation

Goals specified by object categories, room categories, or open-vocabulary semantic descriptions, covering semantic, object-goal, and open-vocabulary navigation.

- [APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_APEX_A_Decoupled_Memory-based_Explorer_for_Asynchronous_Aerial_Object_Goal_CVPR_2026_paper.html), Zhang et al., CVPR 2026.

- [Memory-Augmented Scene Understanding and Exploration for Open-World Aerial Object-Goal Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Memory-Augmented_Scene_Understanding_and_Exploration_for_Open-World_Aerial_Object-Goal_Navigation_CVPR_2026_paper.html), Zhou et al., CVPR 2026.

- [TrajRAG: Retrieving Geometric-Semantic Experience for Zero-Shot Object Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_TrajRAG_Retrieving_Geometric-Semantic_Experience_for_Zero-Shot_Object_Navigation_CVPR_2026_paper.html), Wang et al., CVPR 2026.

- [CogNav: Cognitive Process Modeling for Object Goal Navigation with LLMs](https://openaccess.thecvf.com/content/ICCV2025/html/Cao_CogNav_Cognitive_Process_Modeling_for_Object_Goal_Navigation_with_LLMs_ICCV_2025_paper.html), Cao et al., ICCV 2025.

- [FLaRe: Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-Tuning](https://arxiv.org/abs/2409.16578), Hu et al., ICRA 2025.

- [Function-centric Bayesian Network for Zero-Shot Object Goal Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Function-centric_Bayesian_Network_for_Zero-Shot_Object_Goal_Navigation_ICCV_2025_paper.html), Zhang et al., ICCV 2025.

- [Learning on the Go: A Meta-learning Object Navigation Model](https://openaccess.thecvf.com/content/ICCV2025/html/Qin_Learning_on_the_Go_A_Meta-learning_Object_Navigation_Model_ICCV_2025_paper.html), Qin et al., ICCV 2025.

- [RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_RoboTrom-Nav_A_Unified_Framework_for_Embodied_Navigation_Integrating_Perception_Planning_ICCV_2025_paper.html), Zhong et al., ICCV 2025.

- [TANGO: Training-free Embodied AI Agents for Open-world Tasks](https://openaccess.thecvf.com/content/CVPR2025/html/Ziliotto_TANGO_Training-free_Embodied_AI_Agents_for_Open-world_Tasks_CVPR_2025_paper.html), Ziliotto et al., CVPR 2025.

- [UniGoal: Towards Universal Zero-shot Goal-oriented Navigation](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_UniGoal_Towards_Universal_Zero-shot_Goal-oriented_Navigation_CVPR_2025_paper.html), Yin et al., CVPR 2025.

- [Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation](https://doi.org/10.1109/LRA.2023.3346800), Dorbala et al., RA-L 2024.

- [Imagine Before Go: Self-Supervised Generative Map for Object Goal Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhang_Imagine_Before_Go_Self-Supervised_Generative_Map_for_Object_Goal_Navigation_CVPR_2024_paper.html), Zhang et al., CVPR 2024.

- [MOPA: Modular Object Navigation With PointGoal Agents](https://openaccess.thecvf.com/content/WACV2024/html/Raychaudhuri_MOPA_Modular_Object_Navigation_With_PointGoal_Agents_WACV_2024_paper.html), Raychaudhuri et al., WACV 2024.

- [PoliFormer: Scaling On-Policy RL with Transformers Results in Masterful Navigators](https://arxiv.org/abs/2406.20083), Zeng et al., CoRL 2024.

- [SayNav: Grounding Large Language Models for Dynamic Planning to Navigation in New Environments](https://arxiv.org/abs/2309.04077), Rajvanshi et al., ICAPS 2024.

- [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189), Yin et al., NeurIPS 2024.

- [SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World](https://openaccess.thecvf.com/content/CVPR2024/html/Ehsani_SPOC_Imitating_Shortest_Paths_in_Simulation_Enables_Effective_Navigation_and_CVPR_2024_paper.html), Ehsani et al., CVPR 2024.

- [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.03275), Yokoyama et al., ICRA 2024.

- [VoroNav: Voronoi-based Zero-shot Object Navigation with Large Language Model](https://arxiv.org/abs/2401.02695), Wu et al., ICML 2024.

- [Audio Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2303.07522), Huang et al., ISER 2023.

- [CoWs on Pasture: Baselines and Benchmarks for Language-Driven Zero-Shot Object Navigation](https://openaccess.thecvf.com/content/CVPR2023/html/Gadre_CoWs_on_Pasture_Baselines_and_Benchmarks_for_Language-Driven_Zero-Shot_Object_CVPR_2023_paper.html), Gadre et al., CVPR 2023.

- [ESC: Exploration with Soft Commonsense Constraints for Zero-shot Object Navigation](https://arxiv.org/abs/2301.13166), Zhou et al., ICML 2023.

- [L3MVN: Leveraging Large Language Models for Visual Target Navigation](https://arxiv.org/abs/2304.05501), Yu et al., IROS 2023.

- [PIRLNav: Pretraining With Imitation and RL Finetuning for ObjectNav](https://openaccess.thecvf.com/content/CVPR2023/html/Ramrakhya_PIRLNav_Pretraining_With_Imitation_and_RL_Finetuning_for_ObjectNav_CVPR_2023_paper.html), Ramrakhya et al., CVPR 2023.

- [Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714), Huang et al., ICRA 2023.

- [Habitat-Web: Learning Embodied Object-Search Strategies From Human Demonstrations at Scale](https://openaccess.thecvf.com/content/CVPR2022/html/Ramrakhya_Habitat-Web_Learning_Embodied_Object-Search_Strategies_From_Human_Demonstrations_at_Scale_CVPR_2022_paper.html), Ramrakhya et al., CVPR 2022.

- [PONI: Potential Functions for ObjectGoal Navigation With Interaction-Free Learning](https://openaccess.thecvf.com/content/CVPR2022/html/Ramakrishnan_PONI_Potential_Functions_for_ObjectGoal_Navigation_With_Interaction-Free_Learning_CVPR_2022_paper.html), Ramakrishnan et al., CVPR 2022.

- [Zero Experience Required: Plug & Play Modular Transfer Learning for Semantic Visual Navigation](https://openaccess.thecvf.com/content/CVPR2022/html/Al-Halah_Zero_Experience_Required_Plug__Play_Modular_Transfer_Learning_for_CVPR_2022_paper.html), Al-Halah et al., CVPR 2022.

- [ZSON: Zero-Shot Object-Goal Navigation using Multimodal Goal Embeddings](https://arxiv.org/abs/2206.12403), Majumdar et al., NeurIPS 2022.

- [Auxiliary Tasks and Exploration Enable ObjectGoal Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Ye_Auxiliary_Tasks_and_Exploration_Enable_ObjectGoal_Navigation_ICCV_2021_paper.html), Ye et al., ICCV 2021.

- [Learning to Map for Active Semantic Goal Navigation](https://arxiv.org/abs/2106.15648), Georgakis et al., arXiv 2021.

- [THDA: Treasure Hunt Data Augmentation for Semantic Navigation](https://openaccess.thecvf.com/content/ICCV2021/html/Maksymets_THDA_Treasure_Hunt_Data_Augmentation_for_Semantic_Navigation_ICCV_2021_paper.html), Maksymets et al., ICCV 2021.

- [VTNet: Visual Transformer Network for Object Goal Navigation](https://arxiv.org/abs/2105.09447), Du et al., ICLR 2021.

- [Object Goal Navigation using Goal-Oriented Semantic Exploration](https://arxiv.org/abs/2007.00643), Chaplot et al., NeurIPS 2020.

- [Bayesian Relational Memory for Semantic Visual Navigation](https://openaccess.thecvf.com/content_ICCV_2019/html/Wu_Bayesian_Relational_Memory_for_Semantic_Visual_Navigation_ICCV_2019_paper.html), Wu et al., ICCV 2019.

- [Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning](https://arxiv.org/abs/1812.00971), Wortsman et al., CVPR 2019.

- [Visual Semantic Navigation using Scene Priors](https://arxiv.org/abs/1810.06543), Yang et al., ICLR 2019.

<a id="section-2-4"></a>

### 2.4 Language-Guided Navigation

Navigation from natural-language goals, route instructions, or multi-turn dialogue across discrete and continuous indoor and outdoor environments, including foundation model-based approaches.

- [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_AwareVLN_Reasoning_with_Self-awareness_for_Vision-Language_Navigation_CVPR_2026_paper.html), Guo et al., CVPR 2026.

- [Bridging the 2D-3D Gap: A Hierarchical Semantic-Geometric Map for Vision Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Bridging_the_2D-3D_Gap_A_Hierarchical_Semantic-Geometric_Map_for_Vision_CVPR_2026_paper.html), Li et al., CVPR 2026.

- [DecoVLN: Decoupling Observation, Reasoning, and Correction for Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Xin_DecoVLN_Decoupling_Observation_Reasoning_and_Correction_for_Vision-and-Language_Navigation_CVPR_2026_paper.html), Xin et al., CVPR 2026.

- [DriveVLN: Towards Mapless Vision-and-Language Navigation in Autonomous Driving](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_DriveVLN_Towards_Mapless_Vision-and-Language_Navigation_in_Autonomous_Driving_CVPR_2026_paper.html), Guo et al., CVPR 2026.

- [FantasyVLN: Unified Multimodal Chain-of-Thought Reasoning for Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Zuo_FantasyVLN_Unified_Multimodal_Chain-of-Thought_Reasoning_for_Vision-and-Language_Navigation_CVPR_2026_paper.html), Zuo et al., CVPR 2026.

- [Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation](https://arxiv.org/abs/2512.08186), Wei et al., ICLR 2026.

- [History to Future: Evolving Agent with Experience and Thought for Zero-shot Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Dai_History_to_Future_Evolving_Agent_with_Experience_and_Thought_for_CVPR_2026_paper.html), Dai et al., CVPR 2026.

- [HTNav: A Hybrid Navigation Framework with Tiered Structure for Urban Aerial Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Fan_HTNav_A_Hybrid_Navigation_Framework_with_Tiered_Structure_for_Urban_CVPR_2026_paper.html), Fan et al., CVPR 2026.

- [LookasideVLN: Direction-Aware Aerial Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Ning_LookasideVLN_Direction-Aware_Aerial_Vision-and-Language_Navigation_CVPR_2026_paper.html), Ning et al., CVPR 2026.

- [NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_NavForesee_A_Unified_Vision-Language_World_Model_for_Hierarchical_Planning_and_CVPR_2026_paper.html), Liu et al., CVPR 2026.

- [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787), Zhou et al., arXiv 2026.

- [Parse, Search, and Confirmation: Training-Free Aerial Vision-and-Dialog Navigation with Chain-of-Thought Reasoning and Structured Spatial Memory](https://openaccess.thecvf.com/content/CVPR2026/html/Qi_Parse_Search_and_Confirmation_Training-Free_Aerial_Vision-and-Dialog_Navigation_with_Chain-of-Thought_CVPR_2026_paper.html), Qi et al., CVPR 2026.

- [ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_ProFocus_Proactive_Perception_and_Focused_Reasoning_in_Vision-and-Language_Navigation_CVPR_2026_paper.html), Xue et al., CVPR 2026.

- [Progress-Think: Semantic Progress Reasoning for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Wang_Progress-Think_Semantic_Progress_Reasoning_for_Vision-Language_Navigation_CVPR_2026_paper.html), Wang et al., CVPR 2026.

- [Robostral Navigate](https://arxiv.org/abs/2607.20785), Bounhar et al., arXiv 2026.

- [SimpleVLN: Towards Simple and Frontier Vision-Language Navigation](https://arxiv.org/abs/2610.23203), Hong et al., arXiv 2026.

- [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://doi.org/10.1109/icra57385.2026.11696190), Wei et al., ICRA 2026.

- [Towards Open Environments and Instructions: General Vision-Language Navigation via Fast-Slow Interactive Reasoning](https://openaccess.thecvf.com/content/CVPR2026/html/Li_Towards_Open_Environments_and_Instructions_General_Vision-Language_Navigation_via_Fast-Slow_CVPR_2026_paper.html), Li et al., CVPR 2026.

- [COSMO: Combination of Selective Memorization for Low-cost Vision-and-Language Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_COSMO_Combination_of_Selective_Memorization_for_Low-cost_Vision-and-Language_Navigation_ICCV_2025_paper.html), Zhang et al., ICCV 2025.

- [Do Visual Imaginations Improve Vision-and-Language Navigation Agents?](https://openaccess.thecvf.com/content/CVPR2025/html/Perincherry_Do_Visual_Imaginations_Improve_Vision-and-Language_Navigation_Agents_CVPR_2025_paper.html), Perincherry et al., CVPR 2025.

- [ETPNav: Evolving Topological Planning for Vision-Language Navigation in Continuous Environments](https://doi.org/10.1109/tpami.2024.3386695), An et al., TPAMI 2025.

- [monoVLN: Bridging the Observation Gap between Monocular and Panoramic Vision and Language Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Lu_monoVLN_Bridging_the_Observation_Gap_between_Monocular_and_Panoramic_Vision_ICCV_2025_paper.html), Lu et al., ICCV 2025.

- [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://doi.org/10.15607/rss.2025.xxi.018), Cheng et al., RSS 2025.

- [NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_NavMorph_A_Self-Evolving_World_Model_for_Vision-and-Language_Navigation_in_Continuous_ICCV_2025_paper.html), Yao et al., ICCV 2025.

- [NavQ: Learning a Q-Model for Foresighted Vision-and-Language Navigation](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_NavQ_Learning_a_Q-Model_for_Foresighted_Vision-and-Language_Navigation_ICCV_2025_paper.html), Xu et al., ICCV 2025.

- [SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_SAME_Learning_Generic_Language-Guided_Visual_Navigation_with_State-Adaptive_Mixture_of_ICCV_2025_paper.html), Zhou et al., ICCV 2025.

- [Towards Long-Horizon Vision-Language Navigation: Platform, Benchmark and Method](https://openaccess.thecvf.com/content/CVPR2025/html/Song_Towards_Long-Horizon_Vision-Language_Navigation_Platform_Benchmark_and_Method_CVPR_2025_paper.html), Song et al., CVPR 2025.

- [Lookahead Exploration with Neural Radiance Representation for Continuous Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Wang_Lookahead_Exploration_with_Neural_Radiance_Representation_for_Continuous_Vision-Language_Navigation_CVPR_2024_paper.html), Wang et al., CVPR 2024.

- [NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](https://arxiv.org/abs/2407.12366), Zhou et al., ECCV 2024.

- [NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models](https://doi.org/10.1609/aaai.v38i7.28597), Zhou et al., AAAI 2024.

- [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852), Zhang et al., RSS 2024.

- [OVER-NAV: Elevating Iterative Vision-and-Language Navigation with Open-Vocabulary Detection and StructurEd Representation](https://openaccess.thecvf.com/content/CVPR2024/html/Zhao_OVER-NAV_Elevating_Iterative_Vision-and-Language_Navigation_with_Open-Vocabulary_Detection_and_StructurEd_CVPR_2024_paper.html), Zhao et al., CVPR 2024.

- [Volumetric Environment Representation for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Volumetric_Environment_Representation_for_Vision-Language_Navigation_CVPR_2024_paper.html), Liu et al., CVPR 2024.

- [A New Path: Scaling Vision-and-Language Navigation With Synthetic Instructions and Imitation Learning](https://openaccess.thecvf.com/content/CVPR2023/html/Kamath_A_New_Path_Scaling_Vision-and-Language_Navigation_With_Synthetic_Instructions_and_CVPR_2023_paper.html), Kamath et al., CVPR 2023.

- [BEVBert: Multimodal Map Pre-training for Language-guided Navigation](https://arxiv.org/abs/2212.04385), An et al., ICCV 2023.

- [Iterative Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2023/html/Krantz_Iterative_Vision-and-Language_Navigation_CVPR_2023_paper.html), Krantz et al., CVPR 2023.

- [Bridging the Gap Between Learning in Discrete and Continuous Environments for Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2022/html/Hong_Bridging_the_Gap_Between_Learning_in_Discrete_and_Continuous_Environments_CVPR_2022_paper.html), Hong et al., CVPR 2022.

- [Think Global, Act Local: Dual-Scale Graph Transformer for Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2022/html/Chen_Think_Global_Act_Local_Dual-Scale_Graph_Transformer_for_Vision-and-Language_Navigation_CVPR_2022_paper.html), Chen et al., CVPR 2022.

- [History Aware Multimodal Transformer for Vision-and-Language Navigation](https://arxiv.org/abs/2110.13309), Chen et al., NeurIPS 2021.

- [VLN BERT: A Recurrent Vision-and-Language BERT for Navigation](https://openaccess.thecvf.com/content/CVPR2021/html/Hong_VLN_BERT_A_Recurrent_Vision-and-Language_BERT_for_Navigation_CVPR_2021_paper.html), Hong et al., CVPR 2021.

- [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](https://arxiv.org/abs/2004.02857), Krantz et al., ECCV 2020.

- [Learning to Navigate Unseen Environments: Back Translation with Environmental Dropout](https://arxiv.org/abs/1904.04195), Tan et al., NAACL-HLT 2019.

- [Self-Monitoring Navigation Agent via Auxiliary Progress Estimation](https://arxiv.org/abs/1901.03035), Ma et al., ICLR 2019.

- [Vision-and-Dialog Navigation](https://proceedings.mlr.press/v100/thomason20a.html), Thomason et al., CoRL 2019.

- [Speaker-Follower Models for Vision-and-Language Navigation](https://arxiv.org/abs/1806.02724), Fried et al., NeurIPS 2018.

- [Vision-and-Language Navigation: Interpreting visually-grounded navigation instructions in real environments](https://arxiv.org/abs/1711.07280), Anderson et al., CVPR 2018.

<a id="section-2-5"></a>

### 2.5 Autonomous Exploration

Actions selected to acquire information, discover unknown areas, or build maps, covering single-robot and multi-robot exploration with geometric planning and learned policies.

- [Connectivity-Aware Graph Extension for Decentralized Multi-Robot Exploration](https://arxiv.org/abs/2609.00804), Garcia Cegarra et al., arXiv 2026.

- [FARE: Fast-Slow Agentic Robotic Exploration](https://arxiv.org/abs/2601.14681), Liao et al., arXiv 2026.

- [GUIDE: A Diffusion-Based Autonomous Robot Exploration Framework Using Global Graph Inference](https://doi.org/10.1109/icra57385.2026.11696780), Che et al., ICRA 2026.

- [Planner-Conditioned Diffusion for Coordinated Multi-Agent Exploration](https://arxiv.org/abs/2608.16229), Teo et al., arXiv 2026.

- [WOLF: World Model Guided LiDAR Exploration with Predictive Frontiers](https://arxiv.org/abs/2609.23656), Tian et al., arXiv 2026.

- [A Hierarchical Region-Based Approach for Efficient Multi-Robot Exploration](https://arxiv.org/abs/2503.12876), Meng et al., arXiv 2025.

- [Active perception network for non-myopic online exploration and visual surface coverage](https://doi.org/10.1177/02783649241264577), Vutetakis et al., IJRR 2025.

- [DARE: Diffusion Policy for Autonomous Robot Exploration](https://doi.org/10.1109/icra55743.2025.11128196), Cao et al., ICRA 2025.

- [EPIC: A Lightweight LiDAR-Based UAV Exploration Framework for Large-Scale Scenarios](https://arxiv.org/abs/2410.14203), Geng et al., RA-L 2025.

- [FALCON: Fast Autonomous Aerial Exploration Using Coverage Path Guidance](https://doi.org/10.1109/tro.2024.3522148), Zhang et al., TRO 2025.

- [HDPlanner: Advancing Autonomous Deployments in Unknown Environments Through Hierarchical Decision Networks](https://doi.org/10.1109/lra.2024.3506281), Liang et al., RA-L 2025.

- [HEADER: Hierarchical Robot Exploration via Attention-Based Deep Reinforcement Learning with Expert-Guided Reward](https://arxiv.org/abs/2510.15679), Cao et al., arXiv 2025.

- [PIPE Planner: Pathwise Information Gain with Map Predictions for Indoor Robot Exploration](https://doi.org/10.1109/iros60139.2025.11246190), Baek et al., IROS 2025.

- [Fast autonomous exploration with sparse topological graphs in large-scale environments](https://doi.org/10.1007/s41315-023-00318-7), Wei et al., International Journal of Intelligent Robotics and Applications 2024.

- [ARiADNE: A Reinforcement learning approach using Attention-based Deep Networks for Exploration](https://doi.org/10.1109/icra48891.2023.10160565), Cao et al., ICRA 2023.

- [DREAM: Decentralized Reinforcement Learning for Exploration and Efficient Energy Management in Multi-Robot Systems](https://arxiv.org/abs/2309.17433), Patel et al., arXiv 2023.

- [ECHO: An Efficient Heuristic Viewpoint Determination Method on Frontier-Based Autonomous Exploration for Quadrotors](https://doi.org/10.1109/lra.2023.3282783), Yu et al., RA-L 2023.

- [FAEL: Fast Autonomous Exploration for Large-scale Environments With a Mobile Robot](https://doi.org/10.1109/lra.2023.3236573), Huang et al., RA-L 2023.

- [RACER: Rapid Collaborative Exploration With a Decentralized Multi-UAV System](https://doi.org/10.1109/tro.2023.3236945), Zhou et al., TRO 2023.

- [Representation granularity enables time-efficient autonomous exploration in large, complex worlds](https://doi.org/10.1126/scirobotics.adf0970), Cao et al., Science Robotics 2023.

- [UFOExplorer: Fast and Scalable Sampling-Based Exploration With a Graph-Based Planning Structure](https://doi.org/10.1109/lra.2022.3142923), Duberg et al., RA-L 2022.

- [A Multi-Resolution Frontier-Based Planner for Autonomous 3D Exploration](https://doi.org/10.1109/lra.2021.3068923), Batinovic et al., RA-L 2021.

- [DSVP: Dual-Stage Viewpoint Planner for Rapid Exploration by Dynamic Expansion](https://frc.ri.cmu.edu/~zhangji/publications/IROS_2021.pdf), Zhu et al., IROS 2021.

- [Exploration-RRT: A multi-objective Path Planning and Exploration Framework for Unknown and Unstructured Environments](https://doi.org/10.1109/iros51168.2021.9636243), Lindqvist et al., IROS 2021.

- [FUEL: Fast UAV Exploration using Incremental Frontier Structure and Hierarchical Planning](https://arxiv.org/abs/2010.11561), Zhou et al., RA-L 2021.

- [TARE: A Hierarchical Framework for Efficiently Exploring Complex 3D Environments](https://doi.org/10.15607/rss.2021.xvii.018), Cao et al., RSS 2021.

- [Graph‐based subterranean exploration path planning using aerial and legged robots](https://doi.org/10.1002/rob.21993), Dang et al., JFR 2020.

- [Motion Primitives-based Path Planning for Fast and Agile Exploration using Aerial Robots](https://doi.org/10.1109/icra40945.2020.9196964), Dharmadhikari et al., ICRA 2020.

- [Occupancy Anticipation for Efficient Exploration and Navigation](https://doi.org/10.1007/978-3-030-58558-7_24), Ramakrishnan et al., ECCV 2020.

- [Efficient Autonomous Exploration Planning of Large-Scale 3-D Environments](https://doi.org/10.1109/lra.2019.2897343), Selin et al., RA-L 2019.

- [Graph-based Path Planning for Autonomous Robotic Exploration in Subterranean Environments](https://doi.org/10.1109/IROS40897.2019.8968151), Dang et al., IROS 2019.

- [Learning Exploration Policies for Navigation](https://arxiv.org/abs/1903.01959), Chen et al., ICLR 2019.

- [Rapid exploration with multi-rotors: A frontier selection method for high speed flight](https://doi.org/10.1109/iros.2017.8206030), Cieslewski et al., IROS 2017.

- [Receding Horizon "Next-Best-View" Planner for 3D Exploration](https://doi.org/10.1109/icra.2016.7487281), Bircher et al., ICRA 2016.

- [Efficient frontier detection for robot exploration](https://doi.org/10.1177/0278364913494911), Keidar et al., IJRR 2014.

- [Coordinated multi-robot exploration](https://doi.org/10.1109/tro.2004.839232), Burgard et al., TRO 2005.

- [Information Gain-based Exploration Using Rao-Blackwellized Particle Filters](https://doi.org/10.15607/rss.2005.i.009), Stachniss et al., RSS 2005.

- [A frontier-based approach for autonomous exploration](https://doi.org/10.1109/cira.1997.613851), Yamauchi, CIRA 1997.

<a id="section-2-6"></a>

### 2.6 Coverage and Inspection

Motion planning for area coverage, surface observation, and inspection, including ground coverage, agricultural operations, aerial inspection, and structural inspection.

- [A novel coverage path planning method based on shrink-wrapping technique for autonomous inspection of complex structures using unmanned aerial vehicle](https://doi.org/10.1016/j.rcim.2025.103149), Kaleci et al., Robotics and Computer-Integrated Manufacturing 2026.

- [Multi-Agent Reinforcement Learning for Zero-Shot Coverage Path Planning with Dynamic UAV Networks](https://doi.org/10.1016/j.robot.2025.105163), Carvalho et al., Robotics and Autonomous Systems 2026.

- [Priority-Aware Multi-Robot Coverage Path Planning](https://doi.org/10.1109/lra.2026.3653321), Lee et al., RA-L 2026.

- [TRACE: Coverage Path Planning for Unknown Environments Using Hierarchical Coverage Tree](https://arxiv.org/abs/2609.21777), Shen et al., arXiv 2026.

- [Complete‐coverage path planning for surface inspection of cable‐stayed bridge tower based on building information models and climbing robots](https://doi.org/10.1111/mice.13469), Xia et al., Computer-Aided Civil and Infrastructure Engineering 2025.

- [Deep Reinforcement Learning for Zero-Shot Coverage Path Planning With Mobile Robots](https://doi.org/10.1109/jas.2024.125064), Carvalho et al., IEEE/CAA Journal of Automatica Sinica 2025.

- [Online Concurrent Multi-Robot Coverage Path Planning](https://doi.org/10.1109/iros60139.2025.11247261), Mitra et al., IROS 2025.

- [Sim-to-Real Transfer of Deep Reinforcement Learning Agents for Online Coverage Path Planning](https://doi.org/10.1109/access.2025.3581035), Jonnarth et al., IEEE Access 2025.

- [Fields2Cover: An Open-Source Coverage Path Planning Library for Unmanned Agricultural Vehicles](https://doi.org/10.1109/lra.2023.3248439), Mier et al., RA-L 2023.

- [Scalable Coverage Path Planning of Multi-Robot Teams for Monitoring Non-Convex Areas](https://arxiv.org/abs/2103.14709), Collins et al., ICRA 2021.

- [Multi-UAV Coverage Path Planning for the Inspection of Large and Complex Structures](https://arxiv.org/abs/2007.13065), Jing et al., IROS 2020.

- [DARP: Divide Areas Algorithm for Optimal Multi-Robot Coverage Path Planning](https://doi.org/10.1007/s10846-016-0461-x), Kapoutsis et al., Journal of Intelligent & Robotic Systems 2017.

- [Efficient multi-robot coverage of a known environment](https://doi.org/10.1109/iros.2017.8206000), Karapetyan et al., IROS 2017.

- [Multiobjective coverage path planning: Enabling automated inspection of complex, real-world structures](https://doi.org/10.1016/j.asoc.2017.07.051), Ellefsen et al., Applied Soft Computing 2017.

- [Three-dimensional coverage path planning via viewpoint resampling and tour optimization for aerial robots](https://doi.org/10.1007/s10514-015-9517-1), Bircher et al., Autonomous Robots 2016.

- [Energy-Aware Coverage Path Planning of UAVs](https://doi.org/10.1109/icarsc.2015.17), Di Franco et al., ICARSC 2015.

- [Structural inspection path planning via iterative viewpoint resampling with application to aerial robotics](https://doi.org/10.1109/icra.2015.7140101), Bircher et al., ICRA 2015.

- [Spiral-STC: an on-line coverage algorithm of grid environments by a mobile robot](https://doi.org/10.1109/robot.2002.1013479), Gabriely et al., ICRA 2002.

- [Spanning-tree based coverage of continuous areas by a mobile robot](https://doi.org/10.1109/robot.2001.932890), Gabriely et al., ICRA 2001.

- [Coverage Path Planning: The Boustrophedon Cellular Decomposition](https://www.ri.cmu.edu/pub_files/pub4/choset_howie_1997_3/choset_howie_1997_3.pdf), Choset et al., FSR 1997.

<a id="section-2-7"></a>

### 2.7 Moving Target Following

Continuous following of moving people or objects, including person following, target reacquisition after occlusion, embodied visual tracking, and aerial cinematography.

- [A Shopping Service Robot Framework With Visual-WEM Tracking and Intersection-Aware Following](https://doi.org/10.1109/lra.2026.3668142), Yao et al., RA-L 2026.

- [Adap-RPF: Adaptive Trajectory Sampling for Robot Person Following in Dynamic Crowded Environments](https://doi.org/10.1109/icra57385.2026.11696330), Situ et al., ICRA 2026.

- [CST-WM: A Causally Structured World Model for Embodied Visual Tracking](https://arxiv.org/abs/2609.06302), Hu et al., arXiv 2026.

- [Future-Aware Flow Planning for Safe UAV Target Following](https://arxiv.org/abs/2609.10166), Feng et al., arXiv 2026.

- [USS: Unifying Spatial-Semantic Prompting for End to End Embodied Visual Tracking](https://arxiv.org/abs/2606.25880), Xie et al., arXiv 2026.

- [Vision-Based Person-Following Algorithm for Assistive Elderly-Care Quadruped Robots](https://doi.org/10.3390/s26103263), Kurumbaparambil et al., Sensors 2026.

- [Obstacle-Avoidant Leader Following with a Quadruped Robot](https://doi.org/10.1109/icra55743.2025.11127912), Scheidemann et al., ICRA 2025.

- [Position Based Camera-2D LiDAR Fusion and Person Following for Mobile Robots](https://doi.org/10.1109/icorr66766.2025.11062955), Maslim et al., ICORR 2025.

- [RPF-Search: Field-Based Search for Robot Person Following in Unknown Dynamic Environments](https://doi.org/10.1109/tmech.2025.3588874), Ye et al., T-MECH 2025.

- [TrackVLA: Embodied Visual Tracking in the Wild](https://proceedings.mlr.press/v305/wang25f.html), Wang et al., CoRL 2025.

- [A Dual Closed-Loop Control Strategy for Human-Following Robots Respecting Social Space](https://doi.org/10.1109/icra57147.2024.10611263), Peng et al., ICRA 2024.

- [Follow Anything: Open-Set Detection, Tracking, and Following in Real-Time](https://doi.org/10.1109/lra.2024.3366013), Maalouf et al., RA-L 2024.

- [Person Re-Identification for Robot Person Following With Online Continual Learning](https://doi.org/10.1109/lra.2024.3438042), Ye et al., RA-L 2024.

- [Auto Filmer: Autonomous Aerial Videography Under Human Interaction](https://doi.org/10.1109/lra.2022.3231828), Zhang et al., RA-L 2023.

- [FollowMe: a Robust Person Following Framework Based on Visual Re-Identification and Gestures](https://doi.org/10.1109/arso56563.2023.10187536), Rollo et al., ARSO 2023.

- [MPC-Based Human-Accompanying Control Strategy for Improving the Motion Coordination Between the Target Person and the Robot](https://doi.org/10.1109/iros55552.2023.10342246), Peng et al., IROS 2023.

- [Following Closely: A Robust Monocular Person Following System for Mobile Robot](https://arxiv.org/abs/2204.10540), Ye et al., arXiv 2022.

- [Fast-Tracker: A Robust Aerial System for Tracking Agile Target in Cluttered Environments](https://doi.org/10.1109/icra48506.2021.9561948), Han et al., ICRA 2021.

- [Visibility-aware Trajectory Optimization with Application to Aerial Tracking](https://doi.org/10.1109/iros51168.2021.9636753), Wang et al., IROS 2021.

- [Autonomous Person-Specific Following Robot](https://arxiv.org/abs/2010.08017), Chan et al., ACRA 2020.

- [Real-Time Motion Planning for Aerial Videography With Dynamic Obstacle Avoidance and Viewpoint Optimization](https://doi.org/10.1109/lra.2017.2665693), Nageli et al., RA-L 2017.

- [Person following with a mobile robot using binocular feature-based tracking](https://doi.org/10.1109/iros.2007.4399459), Chen et al., IROS 2007.

<a id="section-3"></a>

## 3. Navigation Methods and Core Capabilities

<a id="section-3-1"></a>

### 3.1 Foundation Model-Based Navigation

Pretrained language, vision-language, and vision-language-action models for goal understanding, semantic grounding, navigation reasoning, planning, and action generation.

- [ABot-N0: Technical Report on the VLA Foundation Model for Versatile Embodied Navigation](https://arxiv.org/abs/2602.11598), Chu et al., arXiv 2026.

- [AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild](https://arxiv.org/abs/2602.09657), Sun et al., ICLR 2026.

- [AwareVLN: Reasoning with Self-awareness for Vision-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Guo_AwareVLN_Reasoning_with_Self-awareness_for_Vision-Language_Navigation_CVPR_2026_paper.html), Guo et al., CVPR 2026.

- [Embodied Navigation Foundation Model](https://arxiv.org/abs/2509.12129), Zhang et al., ICLR 2026.

- [Ground Slow, Move Fast: A Dual-System Foundation Model for Generalizable Vision-and-Language Navigation](https://arxiv.org/abs/2512.08186), Wei et al., ICLR 2026.

- [NavGPT-3: Harnessing Context in a Hierarchical Navigation Runtime](https://arxiv.org/abs/2610.10787), Zhou et al., arXiv 2026.

- [OmniVLA: An Omni-Modal Vision-Language-Action Model for Robot Navigation](https://doi.org/10.1109/icra57385.2026.11697566), Hirose et al., ICRA 2026.

- [ProFocus: Proactive Perception and Focused Reasoning in Vision-and-Language Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Xue_ProFocus_Proactive_Perception_and_Focused_Reasoning_in_Vision-and-Language_Navigation_CVPR_2026_paper.html), Xue et al., CVPR 2026.

- [Robostral Navigate](https://arxiv.org/abs/2607.20785), Bounhar et al., arXiv 2026.

- [SimpleVLN: Towards Simple and Frontier Vision-Language Navigation](https://arxiv.org/abs/2610.23203), Hong et al., arXiv 2026.

- [StreamVLN: Streaming Vision-and-Language Navigation via SlowFast Context Modeling](https://doi.org/10.1109/icra57385.2026.11696190), Wei et al., ICRA 2026.

- [VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory](https://doi.org/10.1109/tro.2026.3747248), Wang et al., TRO 2026.

- [End-to-End Navigation with Vision-Language Models: Transforming Spatial Reasoning into Question-Answering](https://proceedings.mlr.press/v288/goetting25a.html), Goetting et al., International Conference on Neuro-symbolic Systems 2025.

- [Nav-R1: Reasoning and Navigation in Embodied Scenes](https://arxiv.org/abs/2509.10884), Liu et al., arXiv 2025.

- [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://doi.org/10.15607/rss.2025.xxi.018), Cheng et al., RSS 2025.

- [RoboTron-Nav: A Unified Framework for Embodied Navigation Integrating Perception, Planning, and Prediction](https://openaccess.thecvf.com/content/ICCV2025/html/Zhong_RoboTrom-Nav_A_Unified_Framework_for_Embodied_Navigation_Integrating_Perception_Planning_ICCV_2025_paper.html), Zhong et al., ICCV 2025.

- [TrackVLA: Embodied Visual Tracking in the Wild](https://proceedings.mlr.press/v305/wang25f.html), Wang et al., CoRL 2025.

- [Uni-NaVid: A Video-based Vision-Language-Action Model for Unifying Embodied Navigation Tasks](https://doi.org/10.15607/rss.2025.xxi.013), Zhang et al., RSS 2025.

- [UniGoal: Towards Universal Zero-shot Goal-oriented Navigation](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_UniGoal_Towards_Universal_Zero-shot_Goal-oriented_Navigation_CVPR_2025_paper.html), Yin et al., CVPR 2025.

- [VLN-R1: Vision-Language Navigation via Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.17221), Qi et al., arXiv 2025.

- [Can an Embodied Agent Find Your “Cat-shaped Mug”? LLM-Based Zero-Shot Object Navigation](https://doi.org/10.1109/LRA.2023.3346800), Dorbala et al., RA-L 2024.

- [Discuss Before Moving: Visual Language Navigation via Multi-expert Discussions](https://doi.org/10.1109/icra57147.2024.10611565), Long et al., ICRA 2024.

- [Follow Anything: Open-Set Detection, Tracking, and Following in Real-Time](https://doi.org/10.1109/lra.2024.3366013), Maalouf et al., RA-L 2024.

- [MapGPT: Map-Guided Prompting with Adaptive Path Planning for Vision-and-Language Navigation](https://doi.org/10.18653/v1/2024.acl-long.529), Chen et al., ACL 2024.

- [NavAgent: Multi-scale Urban Street View Fusion For UAV Embodied Vision-and-Language Navigation](https://arxiv.org/abs/2411.08579), Liu et al., arXiv 2024.

- [NavGPT-2: Unleashing Navigational Reasoning Capability for Large Vision-Language Models](https://arxiv.org/abs/2407.12366), Zhou et al., ECCV 2024.

- [NavGPT: Explicit Reasoning in Vision-and-Language Navigation with Large Language Models](https://doi.org/10.1609/aaai.v38i7.28597), Zhou et al., AAAI 2024.

- [NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation](https://arxiv.org/abs/2402.15852), Zhang et al., RSS 2024.

- [SayNav: Grounding Large Language Models for Dynamic Planning to Navigation in New Environments](https://arxiv.org/abs/2309.04077), Rajvanshi et al., ICAPS 2024.

- [SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation](https://arxiv.org/abs/2410.08189), Yin et al., NeurIPS 2024.

- [VLFM: Vision-Language Frontier Maps for Zero-Shot Semantic Navigation](https://arxiv.org/abs/2312.03275), Yokoyama et al., ICRA 2024.

- [VoroNav: Voronoi-based Zero-shot Object Navigation with Large Language Model](https://arxiv.org/abs/2401.02695), Wu et al., ICML 2024.

- [Audio Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2303.07522), Huang et al., ISER 2023.

- [CoWs on Pasture: Baselines and Benchmarks for Language-Driven Zero-Shot Object Navigation](https://openaccess.thecvf.com/content/CVPR2023/html/Gadre_CoWs_on_Pasture_Baselines_and_Benchmarks_for_Language-Driven_Zero-Shot_Object_CVPR_2023_paper.html), Gadre et al., CVPR 2023.

- [ESC: Exploration with Soft Commonsense Constraints for Zero-shot Object Navigation](https://arxiv.org/abs/2301.13166), Zhou et al., ICML 2023.

- [L3MVN: Leveraging Large Language Models for Visual Target Navigation](https://arxiv.org/abs/2304.05501), Yu et al., IROS 2023.

- [Visual Language Maps for Robot Navigation](https://arxiv.org/abs/2210.05714), Huang et al., ICRA 2023.

- [CLIP-Nav: Using CLIP for Zero-Shot Vision-and-Language Navigation](https://arxiv.org/abs/2211.16649), Dorbala et al., CoRL Workshops 2022.

- [LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://proceedings.mlr.press/v205/shah23b.html), Shah et al., CoRL 2022.

- [ZSON: Zero-Shot Object-Goal Navigation using Multimodal Goal Embeddings](https://arxiv.org/abs/2206.12403), Majumdar et al., NeurIPS 2022.

<a id="section-3-2"></a>

### 3.2 World Model-Based Navigation

Action-conditioned prediction, latent dynamics, and imagined future observations for navigation planning, policy learning, and closed-loop decision making.

- [Acting from Belief, Looking When Needed: A Bayesian Spatial World Model for Navigation under Intermittent Perception](https://arxiv.org/abs/2610.11591), Yang et al., arXiv 2026.

- [An Efficient and Multi-Modal Navigation System with One-Step World Model](https://arxiv.org/abs/2601.12277), Shen et al., arXiv 2026.

- [AquaWAM: A Dynamics-aware World Action Model for Underwater Embodied Agents](https://arxiv.org/abs/2609.33299), Zhu et al., arXiv 2026.

- [AR Forcing: Towards Long-Horizon Robot Navigation World Model](https://arxiv.org/abs/2605.31314), Yang et al., arXiv 2026.

- [CST-WM: A Causally Structured World Model for Embodied Visual Tracking](https://arxiv.org/abs/2609.06302), Hu et al., arXiv 2026.

- [DeTrack: A Benchmark and Altitude-Aware Dual World Model for Drone-embodied Tracking](https://arxiv.org/abs/2605.17451), Hu et al., arXiv 2026.

- [DiffWAM: A Fast and Efficient Navigation World Action Model](https://arxiv.org/abs/2609.39763), Zhu et al., arXiv 2026.

- [DroneWAM: Efficient World Action Model for Drone Visual Navigation](https://arxiv.org/abs/2609.33148), Yao et al., arXiv 2026.

- [Feeling Terrain Before Crossing: World Models for Off-Road Navigation](https://arxiv.org/abs/2609.19863), Son et al., arXiv 2026.

- [ForeFly: A Dual-Horizon World Action Model for Aerial Vision-Language Navigation](https://arxiv.org/abs/2609.33581), Wang et al., arXiv 2026.

- [G²WAM: World Action Models for Efficient and Geometry Grounded Image-Goal Navigation](https://arxiv.org/abs/2610.16558), Gui et al., arXiv 2026.

- [ImagineUAV: Aerial Vision-Language Navigation via World-Action Modeling and Kinodynamic Planning](https://arxiv.org/abs/2606.01205), Liu et al., arXiv 2026.

- [InJePA: Intention-First Latent Planning with Coupled JEPA World Models for Visual Navigation](https://arxiv.org/abs/2610.23896), Zhou et al., arXiv 2026.

- [LiteNWM: Efficient Latent World Models for Onboard Visual Navigation in the Wild](https://arxiv.org/abs/2610.12368), Liu et al., arXiv 2026.

- [MAD: Mapping-Aware World Models for Agile Quadrotor Flight](https://arxiv.org/abs/2606.04534), Zhang et al., arXiv 2026.

- [MWM: Mobile World Models for Action-Conditioned Consistent Prediction](https://arxiv.org/abs/2603.07799), Yan et al., arXiv 2026.

- [NavForesee: A Unified Vision-Language World Model for Hierarchical Planning and Dual-Horizon Navigation Prediction](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_NavForesee_A_Unified_Vision-Language_World_Model_for_Hierarchical_Planning_and_CVPR_2026_paper.html), Liu et al., CVPR 2026.

- [RAE-NWM: Navigation World Model in Dense Visual Representation Space](https://doi.org/10.1007/978-3-032-37189-8_26), Zhang et al., ECCV 2026.

- [SearchWorld: Spatial Value-Grounded Imagination for UAV Object Search via World Models](https://arxiv.org/abs/2610.09335), Ji et al., arXiv 2026.

- [SkipWorld: Latent Skip Planning with Distilled World Models for Efficient Visual Navigation](https://arxiv.org/abs/2610.18135), Yang et al., arXiv 2026.

- [Skytopia: Monocular Drone Navigation with Action-Conditioned Latent World Models](https://arxiv.org/abs/2609.26007), Zhang et al., arXiv 2026.

- [Social-WM: Safety-Aware Latent World Models for Robot Social Navigation](https://arxiv.org/abs/2609.40177), Zheng et al., arXiv 2026.

- [Towards Unified World Models for Visual Navigation via Memory-Augmented Planning and Foresight](https://doi.org/10.1007/978-3-032-37553-7_16), Dong et al., ECCV 2026.

- [Verti-WM: A Physics-Aided Exteroceptive World Model for Off-Road Reinforcement Learning](https://arxiv.org/abs/2609.23118), Pan et al., arXiv 2026.

- [WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation](https://arxiv.org/abs/2606.04907), Yang et al., arXiv 2026.

- [WOLF: World Model Guided LiDAR Exploration with Predictive Frontiers](https://arxiv.org/abs/2609.23656), Tian et al., arXiv 2026.

- [World SLAM Model: Joint World Modeling for SLAM and Navigation](https://arxiv.org/abs/2609.32626), Qin et al., arXiv 2026.

- [WorldVLN: Autoregressive World Action Model for Aerial Vision-Language Navigation](https://arxiv.org/abs/2605.15964), Zhao et al., arXiv 2026.

- [Aerial World Model for Long-horizon Visual Generation and Navigation in 3D Space](https://arxiv.org/abs/2512.21887), Zhang et al., arXiv 2025.

- [AstraNav-World: World Model for Foresight Control and Consistency](https://arxiv.org/abs/2512.21714), Chen et al., arXiv 2025.

- [DreamerNav: learning-based autonomous navigation in dynamic indoor environments using world models](https://doi.org/10.3389/frobt.2025.1655171), Shanks et al., Frontiers in Robotics and AI 2025.

- [Efficient Image-Goal Navigation with Representative Latent World Model](https://arxiv.org/abs/2511.11011), Zhang et al., arXiv 2025.

- [NavigateDiff: Visual Predictors are Zero-Shot Navigation Assistants](https://arxiv.org/abs/2502.13894), Qin et al., ICRA 2025.

- [Navigation World Models](https://openaccess.thecvf.com/content/CVPR2025/html/Bar_Navigation_World_Models_CVPR_2025_paper.html), Bar et al., CVPR 2025.

- [NavMorph: A Self-Evolving World Model for Vision-and-Language Navigation in Continuous Environments](https://openaccess.thecvf.com/content/ICCV2025/html/Yao_NavMorph_A_Self-Evolving_World_Model_for_Vision-and-Language_Navigation_in_Continuous_ICCV_2025_paper.html), Yao et al., ICCV 2025.

- [WMNav: Integrating Vision-Language Models into World Models for Object Goal Navigation](https://doi.org/10.1109/iros60139.2025.11246684), Nie et al., IROS 2025.

- [X-MOBILITY: End-To-End Generalizable Navigation via World Modeling](https://doi.org/10.1109/icra55743.2025.11128692), Liu et al., ICRA 2025.

- [DREAMWALKER: Mental Planning for Continuous Vision-Language Navigation](https://doi.org/10.1109/iccv51070.2023.00998), Wang et al., ICCV 2023.

- [Pathdreamer: A World Model for Indoor Navigation](https://doi.org/10.1109/iccv48922.2021.01447), Koh et al., ICCV 2021.

<a id="section-3-3"></a>

### 3.3 End-to-End Navigation and Policy Learning

Supervised learning, imitation learning, reinforcement learning, and generative policies that map observations and goals to navigation actions or waypoints, including policy pretraining, online adaptation, and transfer across robot platforms.

- [GUIDE: A Diffusion-Based Autonomous Robot Exploration Framework Using Global Graph Inference](https://doi.org/10.1109/icra57385.2026.11696780), Che et al., ICRA 2026.

- [NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation](https://arxiv.org/abs/2607.14643), An et al., IROS 2026.

- [NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance](https://doi.org/10.1109/icra57385.2026.11696748), Cai et al., ICRA 2026.

- [NavOL: Navigation Policy with Online Imitation Learning](https://proceedings.mlr.press/v306/wei26f.html), Wei et al., ICML 2026.

- [Safe diffusion Q-learning: A hybrid method combining diffusion model and constrained reinforcement learning for AUV navigation](https://doi.org/10.1016/j.oceaneng.2026.124215), Liu et al., Ocean Engineering 2026.

- [X-NavDP: Generalizing Navigation Diffusion Policy to Novel Behavior and Embodiments with Group Q-score Reweighted Matching](https://arxiv.org/abs/2607.28560), Yang et al., CoRL 2026.

- [DARE: Diffusion Policy for Autonomous Robot Exploration](https://doi.org/10.1109/icra55743.2025.11128196), Cao et al., ICRA 2025.

- [FLaRe: Achieving Masterful and Adaptive Robot Policies with Large-Scale Reinforcement Learning Fine-Tuning](https://arxiv.org/abs/2409.16578), Hu et al., ICRA 2025.

- [Learning Decentralized Multi-Robot PointGoal Navigation](https://doi.org/10.1109/lra.2025.3550798), Soualhi et al., RA-L 2025.

- [Learning on the Go: A Meta-learning Object Navigation Model](https://openaccess.thecvf.com/content/ICCV2025/html/Qin_Learning_on_the_Go_A_Meta-learning_Object_Navigation_Model_ICCV_2025_paper.html), Qin et al., ICCV 2025.

- [NaviDiffusor: Cost-Guided Diffusion Model for Visual Navigation](https://arxiv.org/abs/2504.10003), Zeng et al., ICRA 2025.

- [SAME: Learning Generic Language-Guided Visual Navigation with State-Adaptive Mixture of Experts](https://openaccess.thecvf.com/content/ICCV2025/html/Zhou_SAME_Learning_Generic_Language-Guided_Visual_Navigation_with_State-Adaptive_Mixture_of_ICCV_2025_paper.html), Zhou et al., ICCV 2025.

- [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://arxiv.org/abs/2310.07896), Sridhar et al., ICRA 2024.

- [PoliFormer: Scaling On-Policy RL with Transformers Results in Masterful Navigators](https://arxiv.org/abs/2406.20083), Zeng et al., CoRL 2024.

- [SACSoN: Scalable Autonomous Control for Social Navigation](https://doi.org/10.1109/lra.2023.3329626), Hirose et al., RA-L 2024.

- [SPOC: Imitating Shortest Paths in Simulation Enables Effective Navigation and Manipulation in the Real World](https://doi.org/10.1109/cvpr52733.2024.01537), Ehsani et al., CVPR 2024.

- [ARiADNE: A Reinforcement learning approach using Attention-based Deep Networks for Exploration](https://doi.org/10.1109/icra48891.2023.10160565), Cao et al., ICRA 2023.

- [Champion-level drone racing using deep reinforcement learning](https://doi.org/10.1038/s41586-023-06419-4), Kaufmann et al., Nature 2023.

- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](https://proceedings.mlr.press/v229/stachowicz23a.html), Stachowicz et al., CoRL 2023.

- [GNM: A General Navigation Model to Drive Any Robot](https://doi.org/10.1109/icra48891.2023.10161227), Shah et al., ICRA 2023.

- [OVRL-V2: A simple state-of-art baseline for ImageNav and ObjectNav](https://arxiv.org/abs/2303.07798), Yadav et al., arXiv 2023.

- [ViNT: A Foundation Model for Visual Navigation](https://arxiv.org/abs/2306.14846), Shah et al., CoRL 2023.

- [Habitat-Web: Learning Embodied Object-Search Strategies From Human Demonstrations at Scale](https://openaccess.thecvf.com/content/CVPR2022/html/Ramrakhya_Habitat-Web_Learning_Embodied_Object-Search_Strategies_From_Human_Demonstrations_at_Scale_CVPR_2022_paper.html), Ramrakhya et al., CVPR 2022.

- [BADGR: An Autonomous Self-Supervised Learning-Based Navigation System](https://doi.org/10.1109/lra.2021.3057023), Kahn et al., RA-L 2021.

- [LaND: Learning to Navigate from Disengagements](https://doi.org/10.1109/lra.2021.3060404), Kahn et al., RA-L 2021.

- [Learning High-Speed Flight in the Wild](https://doi.org/10.1126/scirobotics.abg5810), Loquercio et al., Science Robotics 2021.

- [No RL, No Simulation: Learning to Navigate without Navigating](https://arxiv.org/abs/2110.09470), Hahn et al., NeurIPS 2021.

- [Rapid Exploration for Open-World Navigation with Latent Goal Models](https://proceedings.mlr.press/v164/shah22a.html), Shah et al., CoRL 2021.

- [ViNG: Learning Open-World Navigation with Visual Goals](https://doi.org/10.1109/icra48506.2021.9561936), Shah et al., ICRA 2021.

- [Auxiliary Tasks Speed Up Learning PointGoal Navigation](https://arxiv.org/abs/2007.04561), Ye et al., CoRL 2020.

- [Cognitive Mapping and Planning for Visual Navigation](https://doi.org/10.1007/s11263-019-01236-7), Gupta et al., IJCV 2020.

- [DD-PPO: Learning Near-Perfect PointGoal Navigators from 2.5 Billion Frames](https://arxiv.org/abs/1911.00357), Wijmans et al., ICLR 2020.

- [Deep Drone Racing: From Simulation to Reality with Domain Randomization](https://doi.org/10.1109/tro.2019.2942989), Loquercio et al., TRO 2020.

- [Learning Your Way Without Map or Compass: Panoramic Target Driven Visual Navigation](https://arxiv.org/abs/1909.09295), Watkins-Valls et al., IROS 2020.

- [Learning Exploration Policies for Navigation](https://arxiv.org/abs/1903.01959), Chen et al., ICLR 2019.

- [Learning Navigation Behaviors End-to-End with AutoRL](https://doi.org/10.1109/lra.2019.2899918), Chiang et al., RA-L 2019.

- [Learning to Learn How to Learn: Self-Adaptive Visual Navigation Using Meta-Learning](https://arxiv.org/abs/1812.00971), Wortsman et al., CVPR 2019.

- [Learning to Navigate in Cities Without a Map](https://arxiv.org/abs/1804.00168), Mirowski et al., NeurIPS 2018.

- [Learning to Navigate in Complex Environments](https://arxiv.org/abs/1611.03673), Mirowski et al., ICLR 2017.

- [Target-driven Visual Navigation in Indoor Scenes using Deep Reinforcement Learning](https://arxiv.org/abs/1609.05143), Zhu et al., ICRA 2017.

<a id="section-3-4"></a>

### 3.4 Perception, Representation, and Memory

Feature extraction and matching, optical flow and point tracking, depth and 3D perception, traversability estimation, navigation representations, spatial representations, and memory.

- [APEX: A Decoupled Memory-based Explorer for Asynchronous Aerial Object Goal Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhang_APEX_A_Decoupled_Memory-based_Explorer_for_Asynchronous_Aerial_Object_Goal_CVPR_2026_paper.html), Zhang et al., CVPR 2026.

- [Depth Anything 3: Recovering the Visual Space from Any Views](https://arxiv.org/abs/2511.10647), Lin et al., ICLR 2026.

- [Human-like memory empowers embodied robots for long-term object navigation](https://doi.org/10.1038/s44172-026-00767-5), Zhang et al., Communications Engineering 2026.

- [Memory-Augmented Scene Understanding and Exploration for Open-World Aerial Object-Goal Navigation](https://openaccess.thecvf.com/content/CVPR2026/html/Zhou_Memory-Augmented_Scene_Understanding_and_Exploration_for_Open-World_Aerial_Object-Goal_Navigation_CVPR_2026_paper.html), Zhou et al., CVPR 2026.

- [3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning](https://doi.org/10.1109/cvpr52734.2025.01612), Yang et al., CVPR 2025.

- [Continuous 3D Perception Model with Persistent State](https://doi.org/10.1109/cvpr52734.2025.00983), Wang et al., CVPR 2025.

- [CoTracker3: Simpler and Better Point Tracking by Pseudo-Labelling Real Videos](https://doi.org/10.1109/iccv51701.2025.00568), Karaev et al., ICCV 2025.

- [Depth Pro: Sharp Monocular Metric Depth in Less Than a Second](https://arxiv.org/abs/2410.02073), Bochkovskii et al., ICLR 2025.

- [VGGT: Visual Geometry Grounded Transformer](https://doi.org/10.1109/cvpr52734.2025.00499), Wang et al., CVPR 2025.

- [Wild Visual Navigation: Fast Traversability Learning via Pre-Trained Models and Online Self-Supervision](https://doi.org/10.1007/s10514-025-10202-x), Mattamala et al., Autonomous Robots 2025.

- [ConceptGraphs: Open-Vocabulary 3D Scene Graphs for Perception and Planning](https://doi.org/10.1109/icra57147.2024.10610243), Gu et al., ICRA 2024.

- [Depth Anything V2](https://doi.org/10.52202/079017-0688), Yang et al., NeurIPS 2024.

- [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://doi.org/10.1109/cvpr52733.2024.00987), Yang et al., CVPR 2024.

- [DUSt3R: Geometric 3D Vision Made Easy](https://doi.org/10.1109/cvpr52733.2024.01956), Wang et al., CVPR 2024.

- [MemoNav: Working Memory Model for Visual Navigation](https://openaccess.thecvf.com/content/CVPR2024/html/Li_MemoNav_Working_Memory_Model_for_Visual_Navigation_CVPR_2024_paper.html), Li et al., CVPR 2024.

- [SEA-RAFT: Simple, Efficient, Accurate RAFT for Optical Flow](https://doi.org/10.1007/978-3-031-72667-5_3), Wang et al., ECCV 2024.

- [XFeat: Accelerated Features for Lightweight Image Matching](https://doi.org/10.1109/cvpr52733.2024.00259), Potje et al., CVPR 2024.

- [BEVBert: Multimodal Map Pre-training for Language-guided Navigation](https://arxiv.org/abs/2212.04385), An et al., ICCV 2023.

- [ConceptFusion: Open-set Multimodal 3D Mapping](https://doi.org/10.15607/rss.2023.xix.066), Jatavallabhula et al., RSS 2023.

- [Emergence of Maps in the Memories of Blind Navigation Agents](https://arxiv.org/abs/2301.13261), Wijmans et al., ICLR 2023.

- [LightGlue: Local Feature Matching at Light Speed](https://doi.org/10.1109/iccv51070.2023.01616), Lindenberger et al., ICCV 2023.

- [Offline Visual Representation Learning for Embodied Navigation](https://arxiv.org/abs/2204.13226), Yadav et al., ICLR Workshops 2023.

- [TAPIR: Tracking Any Point with per-frame Initialization and temporal Refinement](https://doi.org/10.1109/iccv51070.2023.00923), Doersch et al., ICCV 2023.

- [TerrainNet: Visual Modeling of Complex Terrain for High-speed, Off-road Navigation](https://doi.org/10.15607/rss.2023.xix.103), Meng et al., RSS 2023.

- [Where are we in the search for an Artificial Visual Cortex for Embodied Intelligence?](https://doi.org/10.52202/075280-0031), Majumdar et al., NeurIPS 2023.

- [GMFlow: Learning Optical Flow via Global Matching](https://doi.org/10.1109/cvpr52688.2022.00795), Xu et al., CVPR 2022.

- [Simple but Effective: CLIP Embeddings for Embodied AI](https://doi.org/10.1109/cvpr52688.2022.01441), Khandelwal et al., CVPR 2022.

- [History Aware Multimodal Transformer for Vision-and-Language Navigation](https://arxiv.org/abs/2110.13309), Chen et al., NeurIPS 2021.

- [LoFTR: Detector-Free Local Feature Matching with Transformers](https://doi.org/10.1109/cvpr46437.2021.00881), Sun et al., CVPR 2021.

- [Structured Scene Memory for Vision-Language Navigation](https://doi.org/10.1109/cvpr46437.2021.00835), Wang et al., CVPR 2021.

- [RAFT: Recurrent All-Pairs Field Transforms for Optical Flow](https://doi.org/10.1007/978-3-030-58536-5_24), Teed et al., ECCV 2020.

- [SuperGlue: Learning Feature Matching with Graph Neural Networks](https://doi.org/10.1109/cvpr42600.2020.00499), Sarlin et al., CVPR 2020.

- [Scene Memory Transformer for Embodied Agents in Long-Horizon Tasks](https://doi.org/10.1109/cvpr.2019.00063), Fang et al., CVPR 2019.

- [Neural Map: Structured Memory for Deep Reinforcement Learning](https://arxiv.org/abs/1702.08360), Parisotto et al., ICLR 2018.

- [Semi-parametric Topological Memory for Navigation](https://arxiv.org/abs/1803.00653), Savinov et al., ICLR 2018.

- [SuperPoint: Self-Supervised Interest Point Detection and Description](https://doi.org/10.1109/cvprw.2018.00060), DeTone et al., CVPR Workshops 2018.

<a id="section-3-5"></a>

### 3.5 Odometry and State Estimation

Visual, inertial, LiDAR, radar, and event-camera odometry, together with multi-sensor fusion, motion preintegration, invariant filtering, and state estimation for legged robots.

- [KISS-IMU: Self-supervised Inertial Odometry with Motion-balanced Learning and Uncertainty-aware Inference](https://doi.org/10.1109/icra57385.2026.11697039), Choi et al., ICRA 2026.

- [STEAM-LIVO: Spatio-Temporally Adaptive Manifold Lidar-Inertial-Visual Odometry for Sensor Degradation in Unstructured Natural Aquatic-Terrestrial Scenes](https://doi.org/10.1109/icra57385.2026.11697162), Guo et al., ICRA 2026.

- [Deep Visual Odometry for Stereo Event Cameras](https://doi.org/10.1109/lra.2025.3609095), Zhong et al., RA-L 2025.

- [FAST-LIVO2: Fast, Direct LiDAR–Inertial–Visual Odometry](https://doi.org/10.1109/tro.2024.3502198), Zheng et al., TRO 2025.

- [DBA-Fusion: Tightly Integrating Deep Dense Visual Bundle Adjustment With Multiple Sensors for Large-Scale Localization and Mapping](https://doi.org/10.1109/lra.2024.3400156), Zhou et al., RA-L 2024.

- [R3LIVE++: A Robust, Real-Time, Radiance Reconstruction Package With a Tightly-Coupled LiDAR-Inertial-Visual State Estimator](https://doi.org/10.1109/tpami.2024.3456473), Lin et al., TPAMI 2024.

- [Deep Patch Visual Odometry](https://doi.org/10.52202/075280-1696), Teed et al., NeurIPS 2023.

- [Direct LiDAR-Inertial Odometry: Lightweight LIO with Continuous-Time Motion Correction](https://doi.org/10.1109/icra48891.2023.10160508), Chen et al., ICRA 2023.

- [DytanVO: Joint Refinement of Visual Odometry and Motion Segmentation in Dynamic Environments](https://doi.org/10.1109/icra48891.2023.10161306), Shen et al., ICRA 2023.

- [KISS-ICP: In Defense of Point-to-Point ICP – Simple, Accurate, and Robust Registration If Done the Right Way](https://doi.org/10.1109/lra.2023.3236571), Vizzo et al., RA-L 2023.

- [Lidar-Level Localization With Radar? The CFEAR Approach to Accurate, Fast, and Robust Large-Scale Radar Odometry in Diverse Environments](https://doi.org/10.1109/tro.2022.3221302), Adolfsson et al., TRO 2023.

- [Point‐LIO: Robust High‐Bandwidth Light Detection and Ranging Inertial Odometry](https://doi.org/10.1002/aisy.202200459), He et al., Advanced Intelligent Systems 2023.

- [CT-ICP: Real-time Elastic LiDAR Odometry with Loop Closure](https://doi.org/10.1109/icra46639.2022.9811849), Dellenbach et al., ICRA 2022.

- [FAST-LIO2: Fast Direct LiDAR-Inertial Odometry](https://doi.org/10.1109/tro.2022.3141876), Xu et al., TRO 2022.

- [FAST-LIVO: Fast and Tightly-coupled Sparse-Direct LiDAR-Inertial-Visual Odometry](https://doi.org/10.1109/iros47612.2022.9981107), Zheng et al., IROS 2022.

- [GVINS: Tightly Coupled GNSS–Visual–Inertial Fusion for Smooth and Consistent State Estimation](https://doi.org/10.1109/tro.2021.3133730), Cao et al., TRO 2022.

- [R3LIVE: A Robust, Real-Time, RGB-Colored, LiDAR-Inertial-Visual Tightly-Coupled State Estimation and Mapping Package](https://doi.org/10.1109/icra46639.2022.9811935), Lin et al., ICRA 2022.

- [FAST-LIO: A Fast, Robust LiDAR-Inertial Odometry Package by Tightly-Coupled Iterated Kalman Filter](https://doi.org/10.1109/lra.2021.3064227), Xu et al., RA-L 2021.

- [Contact-aided invariant extended Kalman filtering for robot state estimation](https://doi.org/10.1177/0278364919894385), Hartley et al., IJRR 2020.

- [D3VO: Deep Depth, Deep Pose and Deep Uncertainty for Monocular Visual Odometry](https://doi.org/10.1109/cvpr42600.2020.00136), Yang et al., CVPR 2020.

- [OpenVINS: A Research Platform for Visual-Inertial Estimation](https://doi.org/10.1109/icra40945.2020.9196524), Geneva et al., ICRA 2020.

- [TartanVO: A Generalizable Learning-based VO](https://proceedings.mlr.press/v155/wang21h.html), Wang et al., CoRL 2020.

- [TLIO: Tight Learned Inertial Odometry](https://doi.org/10.1109/lra.2020.3007421), Liu et al., RA-L 2020.

- [Visual-Inertial Mapping With Non-Linear Factor Recovery](https://doi.org/10.1109/lra.2019.2961227), Usenko et al., RA-L 2020.

- [A General Optimization-based Framework for Local Odometry Estimation with Multiple Sensors](https://arxiv.org/abs/1901.03638), Qin et al., arXiv 2019.

- [Direct Sparse Odometry](https://doi.org/10.1109/tpami.2017.2658577), Engel et al., TPAMI 2018.

- [IONet: Learning to Cure the Curse of Drift in Inertial Odometry](https://doi.org/10.1609/aaai.v32i1.12102), Chen et al., AAAI 2018.

- [LeGO-LOAM: Lightweight and Ground-Optimized Lidar Odometry and Mapping on Variable Terrain](https://doi.org/10.1109/iros.2018.8594299), Shan et al., IROS 2018.

- [RIDI: Robust IMU Double Integration](https://doi.org/10.1007/978-3-030-01261-8_38), Yan et al., ECCV 2018.

- [Ultimate SLAM? Combining Events, Images, and IMU for Robust Visual SLAM in HDR and High-Speed Scenarios](https://doi.org/10.1109/lra.2018.2793357), Vidal et al., RA-L 2018.

- [VINS-Mono: A Robust and Versatile Monocular Visual-Inertial State Estimator](https://doi.org/10.1109/tro.2018.2853729), Qin et al., TRO 2018.

- [DeepVO: Towards end-to-end visual odometry with deep Recurrent Convolutional Neural Networks](https://doi.org/10.1109/icra.2017.7989236), Wang et al., ICRA 2017.

- [On-Manifold Preintegration for Real-Time Visual–Inertial Odometry](https://doi.org/10.1109/tro.2016.2597321), Forster et al., TRO 2017.

- [SVO: Semidirect Visual Odometry for Monocular and Multicamera Systems](https://doi.org/10.1109/tro.2016.2623335), Forster et al., TRO 2017.

- [The Invariant Extended Kalman Filter as a Stable Observer](https://doi.org/10.1109/tac.2016.2594085), Barrau et al., TAC 2017.

- [Keyframe-based visual–inertial odometry using nonlinear optimization](https://doi.org/10.1177/0278364914554813), Leutenegger et al., IJRR 2015.

- [Robust visual inertial odometry using a direct EKF-based approach](https://doi.org/10.1109/iros.2015.7353389), Bloesch et al., IROS 2015.

- [LOAM: Lidar Odometry and Mapping in Real-time](https://doi.org/10.15607/rss.2014.x.007), Zhang et al., RSS 2014.

- [State Estimation for Legged Robots - Consistent Fusion of Leg Kinematics and IMU](https://www.roboticsproceedings.org/rss08/p03.html), Bloesch et al., RSS 2012.

- [A Multi-State Constraint Kalman Filter for Vision-aided Inertial Navigation](https://doi.org/10.1109/robot.2007.364024), Mourikis et al., ICRA 2007.

<a id="section-3-6"></a>

### 3.6 Localization and Mapping

Visual and LiDAR SLAM, relocalization and place recognition, loop closure, graph optimization, and mapping with voxels, implicit fields, 3D Gaussians, and semantic scene graphs.

- [DynaGSLAM: Real-Time Gaussian-Splatting SLAM for Online Rendering, Tracking, Motion Predictions of Moving Objects in Dynamic Scenes](https://doi.org/10.1109/wacv61042.2026.00240), Li et al., WACV 2026.

- [ODGS-SLAM: Omnidirectional Gaussian Splatting SLAM](https://openaccess.thecvf.com/content/CVPR2026/html/Spiss_ODGS-SLAM_Omnidirectional_Gaussian_Splatting_SLAM_CVPR_2026_paper.html), Spiss et al., CVPR 2026.

- [VGGT-SLAM 2.0: Real-time Dense Feed-forward Scene Reconstruction](https://doi.org/10.15607/rss.2026.xxii.051), Maggio et al., RSS 2026.

- [AirSLAM: An Efficient and Illumination-Robust Point-Line Visual SLAM System](https://doi.org/10.1109/tro.2025.3539171), Xu et al., TRO 2025.

- [MASt3R-SLAM: Real-Time Dense SLAM with 3D Reconstruction Priors](https://doi.org/10.1109/cvpr52734.2025.01556), Murai et al., CVPR 2025.

- [Reloc3r: Large-Scale Training of Relative Camera Pose Regression for Generalizable, Fast, and Accurate Visual Localization](https://doi.org/10.1109/cvpr52734.2025.01560), Dong et al., CVPR 2025.

- [Splat-SLAM: Globally Optimized RGB-Only SLAM with 3D Gaussians](https://doi.org/10.1109/cvprw67362.2025.00156), Sandström et al., CVPR Workshops 2025.

- [AnyLoc: Towards Universal Visual Place Recognition](https://doi.org/10.1109/lra.2023.3343602), Keetha et al., RA-L 2024.

- [Gaussian Splatting SLAM](https://doi.org/10.1109/cvpr52733.2024.01708), Matsuki et al., CVPR 2024.

- [Optimal Transport Aggregation for Visual Place Recognition](https://doi.org/10.1109/cvpr52733.2024.01672), Izquierdo et al., CVPR 2024.

- [SplaTAM: Splat, Track & Map 3D Gaussians for Dense RGB-D SLAM](https://doi.org/10.1109/cvpr52733.2024.02018), Keetha et al., CVPR 2024.

- [Accelerated Coordinate Encoding: Learning to Relocalize in Minutes Using RGB and Poses](https://doi.org/10.1109/cvpr52729.2023.00488), Brachmann et al., CVPR 2023.

- [Co-SLAM: Joint Coordinate and Sparse Parametric Encodings for Neural Real-Time SLAM](https://doi.org/10.1109/cvpr52729.2023.01277), Wang et al., CVPR 2023.

- [EigenPlaces: Training Viewpoint Robust Models for Visual Place Recognition](https://doi.org/10.1109/iccv51070.2023.01017), Berton et al., ICCV 2023.

- [ESLAM: Efficient Dense SLAM System Based on Hybrid Representation of Signed Distance Fields](https://doi.org/10.1109/cvpr52729.2023.01670), Johari et al., CVPR 2023.

- [Point-SLAM: Dense Neural Point Cloud-based SLAM](https://doi.org/10.1109/iccv51070.2023.01690), Sandström et al., ICCV 2023.

- [Hydra: A Real-time Spatial Perception System for 3D Scene Graph Construction and Optimization](https://doi.org/10.15607/rss.2022.xviii.050), Hughes et al., RSS 2022.

- [LCDNet: Deep Loop Closure Detection and Point Cloud Registration for LiDAR SLAM](https://doi.org/10.1109/tro.2022.3150683), Cattaneo et al., TRO 2022.

- [NICE-SLAM: Neural Implicit Scalable Encoding for SLAM](https://doi.org/10.1109/cvpr52688.2022.01245), Zhu et al., CVPR 2022.

- [OverlapTransformer: An Efficient and Yaw-Angle-Invariant Transformer Network for LiDAR-Based Place Recognition](https://doi.org/10.1109/lra.2022.3178797), Ma et al., RA-L 2022.

- [Rethinking Visual Geo-localization for Large-Scale Applications](https://doi.org/10.1109/cvpr52688.2022.00483), Berton et al., CVPR 2022.

- [DROID-SLAM: Deep Visual SLAM for Monocular, Stereo, and RGB-D Cameras](https://proceedings.neurips.cc/paper/2021/hash/89fcd07f20b6785b92134bd6c1d0fa42-Abstract.html), Teed et al., NeurIPS 2021.

- [iMAP: Implicit Mapping and Positioning in Real-Time](https://doi.org/10.1109/iccv48922.2021.00617), Sucar et al., ICCV 2021.

- [LVI-SAM: Tightly-coupled Lidar-Visual-Inertial Odometry via Smoothing and Mapping](https://doi.org/10.1109/icra48506.2021.9561996), Shan et al., ICRA 2021.

- [ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual–Inertial, and Multimap SLAM](https://doi.org/10.1109/tro.2021.3075644), Campos et al., TRO 2021.

- [TEASER: Fast and Certifiable Point Cloud Registration](https://doi.org/10.1109/tro.2020.3033695), Yang et al., TRO 2021.

- [Kimera: an Open-Source Library for Real-Time Metric-Semantic Localization and Mapping](https://doi.org/10.1109/icra40945.2020.9196885), Rosinol et al., ICRA 2020.

- [LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping](https://doi.org/10.1109/iros45743.2020.9341176), Shan et al., IROS 2020.

- [From Coarse to Fine: Robust Hierarchical Localization at Large Scale](https://doi.org/10.1109/cvpr.2019.01300), Sarlin et al., CVPR 2019.

- [RTAB‐Map as an open‐source lidar and visual simultaneous localization and mapping library for large‐scale and long‐term online operation](https://doi.org/10.1002/rob.21831), Labbé et al., Journal of Field Robotics 2019.

- [Efficient Surfel-Based SLAM using 3D Laser Range Data in Urban Environments](https://www.roboticsproceedings.org/rss14/p16.html), Behley et al., RSS 2018.

- [NetVLAD: CNN Architecture for Weakly Supervised Place Recognition](https://doi.org/10.1109/tpami.2017.2711011), Arandjelovic et al., TPAMI 2018.

- [Scan Context: Egocentric Spatial Descriptor for Place Recognition Within 3D Point Cloud Map](https://doi.org/10.1109/iros.2018.8593953), Kim et al., IROS 2018.

- [BundleFusion: Real-Time Globally Consistent 3D Reconstruction Using On-the-Fly Surface Reintegration](https://doi.org/10.1145/3054739), Dai et al., ACM TOG 2017.

- [ORB-SLAM2: An Open-Source SLAM System for Monocular, Stereo, and RGB-D Cameras](https://doi.org/10.1109/tro.2017.2705103), Mur-Artal et al., TRO 2017.

- [Voxblox: Incremental 3D Euclidean Signed Distance Fields for on-board MAV planning](https://doi.org/10.1109/iros.2017.8202315), Oleynikova et al., IROS 2017.

- [ElasticFusion: Real-time dense SLAM and light source estimation](https://doi.org/10.1177/0278364916669237), Whelan et al., IJRR 2016.

- [Real-time loop closure in 2D LIDAR SLAM](https://doi.org/10.1109/icra.2016.7487258), Hess et al., ICRA 2016.

- [PoseNet: A Convolutional Network for Real-Time 6-DOF Camera Relocalization](https://doi.org/10.1109/iccv.2015.336), Kendall et al., ICCV 2015.

- [LSD-SLAM: Large-Scale Direct Monocular SLAM](https://doi.org/10.1007/978-3-319-10605-2_54), Engel et al., ECCV 2014.

- [OctoMap: an efficient probabilistic 3D mapping framework based on octrees](https://doi.org/10.1007/s10514-012-9321-0), Hornung et al., Autonomous Robots 2013.

- [iSAM2: Incremental smoothing and mapping using the Bayes tree](https://doi.org/10.1177/0278364911430419), Kaess et al., IJRR 2012.

- [DTAM: Dense tracking and mapping in real-time](https://doi.org/10.1109/iccv.2011.6126513), Newcombe et al., ICCV 2011.

- [g2o: A General Framework for Graph Optimization](https://doi.org/10.1109/icra.2011.5979949), Kümmerle et al., ICRA 2011.

- [KinectFusion: Real-time dense surface mapping and tracking](https://doi.org/10.1109/ismar.2011.6092378), Newcombe et al., ISMAR 2011.

<a id="section-3-7"></a>

### 3.7 Path Planning and Decision Making

Heuristic search, sampling-based planning, trajectory optimization, predictive control, collision avoidance, and multi-robot coordination, together with differentiable planning, generative planning, and decision making under uncertainty.

- [Unified Generation-Refinement Planning: Bridging Guided Flow Matching and Sampling-Based MPC for Social Navigation](https://doi.org/10.1109/icra57385.2026.11696822), Mizuta et al., ICRA 2026.

- [Motion Planning Diffusion: Learning and Adapting Robot Motion Planning With Diffusion Models](https://doi.org/10.1109/tro.2025.3593109), Carvalho et al., TRO 2025.

- [Safety-assured high-speed navigation for MAVs](https://doi.org/10.1126/scirobotics.ado6187), Ren et al., Science Robotics 2025.

- [DiPPeR: Diffusion-based 2D Path Planner applied on Legged Robots](https://doi.org/10.1109/icra57147.2024.10610013), Liu et al., ICRA 2024.

- [DiPPeST: Diffusion-based Path Planner for Synthesizing Trajectories Applied on Quadruped Robots](https://doi.org/10.1109/iros58592.2024.10802677), Stamatopoulou et al., IROS 2024.

- [FASTER: Fast and Safe Trajectory Planner for Navigation in Unknown Environments](https://doi.org/10.1109/tro.2021.3100142), Tordesillas et al., TRO 2022.

- [Geometrically Constrained Trajectory Optimization for Multicopters](https://doi.org/10.1109/tro.2022.3160022), Wang et al., TRO 2022.

- [ViKiNG: Vision-Based Kilometer-Scale Navigation with Geographic Hints](https://doi.org/10.15607/rss.2022.xviii.019), Shah et al., RSS 2022.

- [EGO-Planner: An ESDF-Free Gradient-Based Local Planner for Quadrotors](https://doi.org/10.1109/lra.2020.3047728), Zhou et al., RA-L 2021.

- [EGO-Swarm: A Fully Autonomous and Decentralized Quadrotor Swarm System in Cluttered Environments](https://doi.org/10.1109/icra48506.2021.9561902), Zhou et al., ICRA 2021.

- [Motion Planning Networks: Bridging the Gap Between Learning-Based and Classical Motion Planners](https://doi.org/10.1109/tro.2020.3006716), Qureshi et al., TRO 2021.

- [Path Planning using Neural A* Search](https://proceedings.mlr.press/v139/yonetani21a.html), Yonetani et al., ICML 2021.

- [RAPTOR: Robust and Perception-Aware Trajectory Replanning for Quadrotor Fast Flight](https://doi.org/10.1109/tro.2021.3071527), Zhou et al., TRO 2021.

- [Batch Informed Trees (BIT*): Informed asymptotically optimal anytime search](https://doi.org/10.1177/0278364919890396), Gammell et al., IJRR 2020.

- [Robust and Efficient Quadrotor Trajectory Generation for Fast Autonomous Flight](https://doi.org/10.1109/lra.2019.2927938), Zhou et al., RA-L 2019.

- [Continuous-time Gaussian process motion planning via probabilistic inference](https://doi.org/10.1177/0278364918790369), Mukadam et al., IJRR 2018.

- [Information-Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving](https://doi.org/10.1109/tro.2018.2865891), Williams et al., TRO 2018.

- [PRM-RL: Long-range Robotic Navigation Tasks by Combining Reinforcement Learning and Sampling-Based Planning](https://doi.org/10.1109/icra.2018.8461096), Faust et al., ICRA 2018.

- [DESPOT: Online POMDP Planning with Regularization](https://doi.org/10.1613/jair.5328), Ye et al., JAIR 2017.

- [Integrated online trajectory planning and optimization in distinctive topologies](https://doi.org/10.1016/j.robot.2016.11.007), Rösmann et al., Robotics and Autonomous Systems 2017.

- [Planning Dynamically Feasible Trajectories for Quadrotors Using Safe Flight Corridors in 3-D Complex Environments](https://doi.org/10.1109/lra.2017.2663526), Liu et al., RA-L 2017.

- [Value Iteration Networks](https://proceedings.neurips.cc/paper/2016/hash/c21002f464c5fc5bee3b98ced83963b8-Abstract.html), Tamar et al., NeurIPS 2016.

- [Conflict-based search for optimal multi-agent pathfinding](https://doi.org/10.1016/j.artint.2014.11.006), Sharon et al., Artificial Intelligence 2015.

- [Fast marching tree: A fast marching sampling-based method for optimal motion planning in many dimensions](https://doi.org/10.1177/0278364915577958), Janson et al., IJRR 2015.

- [Informed RRT*: Optimal sampling-based path planning focused via direct sampling of an admissible ellipsoidal heuristic](https://doi.org/10.1109/iros.2014.6942976), Gammell et al., IROS 2014.

- [Motion planning with sequential convex optimization and convex collision checking](https://doi.org/10.1177/0278364914528132), Schulman et al., IJRR 2014.

- [CHOMP: Covariant Hamiltonian optimization for motion planning](https://doi.org/10.1177/0278364913488805), Zucker et al., IJRR 2013.

- [LQG-MP: Optimized path planning for robots with motion uncertainty and imperfect state information](https://doi.org/10.1177/0278364911406562), van den Berg et al., IJRR 2011.

- [Minimum snap trajectory generation and control for quadrotors](https://doi.org/10.1109/icra.2011.5980409), Mellinger et al., ICRA 2011.

- [Sampling-based algorithms for optimal motion planning](https://doi.org/10.1177/0278364911406761), Karaman et al., IJRR 2011.

- [SIPP: Safe interval path planning for dynamic environments](https://doi.org/10.1109/icra.2011.5980306), Phillips et al., ICRA 2011.

- [STOMP: Stochastic trajectory optimization for motion planning](https://doi.org/10.1109/icra.2011.5980280), Kalakrishnan et al., ICRA 2011.

- [Path Planning for Autonomous Vehicles in Unknown Semi-structured Environments](https://doi.org/10.1177/0278364909359210), Dolgov et al., IJRR 2010.

- [Theta*: Any-Angle Path Planning on Grids](https://doi.org/10.1613/jair.2994), Daniel et al., JAIR 2010.

- [Reciprocal Velocity Obstacles for real-time multi-agent navigation](https://doi.org/10.1109/robot.2008.4543489), van den Berg et al., ICRA 2008.

- [SARSOP: Efficient Point-Based POMDP Planning by Approximating Optimally Reachable Belief Spaces](https://doi.org/10.15607/rss.2008.iv.009), Kurniawati et al., RSS 2008.

- [Anytime Dynamic A*: An Anytime, Replanning Algorithm](https://cdn.aaai.org/ICAPS/2005/ICAPS05-027.pdf), Likhachev et al., ICAPS 2005.

- [ARA*: Anytime A* with Provable Bounds on Sub-Optimality](https://papers.nips.cc/paper_files/paper/2003/hash/ee8fe9093fbbb687bef15a38facc44d2-Abstract.html), Likhachev et al., NeurIPS 2003.

- [D* Lite](https://www.cs.cmu.edu/~motionplanning/papers/sbp_papers/integrated3/koenig_dstarlite_aaai02b.pdf), Koenig et al., AAAI 2002.

- [RRT-connect: An efficient approach to single-query path planning](https://doi.org/10.1109/robot.2000.844730), Kuffner et al., ICRA 2000.

- [The dynamic window approach to collision avoidance](https://doi.org/10.1109/100.580977), Fox et al., RAM 1997.

- [Probabilistic roadmaps for path planning in high-dimensional configuration spaces](https://doi.org/10.1109/70.508439), Kavraki et al., T-RA 1996.

- [Elastic bands: connecting path planning and control](https://doi.org/10.1109/robot.1993.291936), Quinlan et al., ICRA 1993.

- [The vector field histogram-fast obstacle avoidance for mobile robots](https://doi.org/10.1109/70.88137), Borenstein et al., T-RA 1991.

- [A Formal Basis for the Heuristic Determination of Minimum Cost Paths](https://doi.org/10.1109/tssc.1968.300136), Hart et al., TSSC 1968.

<a id="section-4"></a>

## 4. Robot Platforms

<a id="section-4-1"></a>

### 4.1 Unmanned Aerial Vehicles

Navigation for aerial robots, including language-guided flight, visual homing, drone racing, high-speed obstacle avoidance, trajectory planning, and decentralized swarm flight.

- [AutoFly: Vision-Language-Action Model for UAV Autonomous Navigation in the Wild](https://arxiv.org/abs/2602.09657), Sun et al., ICLR 2026.

- [Efficient robot navigation inspired by honeybee learning flights](https://doi.org/10.1038/s41586-026-10461-3), Ou et al., Nature 2026.

- [Learning vision-based agile flight via differentiable physics](https://doi.org/10.1038/s42256-025-01048-0), Zhang et al., Nature Machine Intelligence 2025.

- [Champion-level drone racing using deep reinforcement learning](https://doi.org/10.1038/s41586-023-06419-4), Kaufmann et al., Nature 2023.

- [FASTER: Fast and Safe Trajectory Planner for Navigation in Unknown Environments](https://doi.org/10.1109/tro.2021.3100142), Tordesillas et al., TRO 2022.

- [Learning high-speed flight in the wild](https://doi.org/10.1126/scirobotics.abg5810), Loquercio et al., Science Robotics 2021.

- [EGO-Planner: An ESDF-Free Gradient-Based Local Planner for Quadrotors](https://doi.org/10.1109/lra.2020.3047728), Zhou et al., RA-L 2021.

- [EGO-Swarm: A Fully Autonomous and Decentralized Quadrotor Swarm System in Cluttered Environments](https://doi.org/10.1109/icra48506.2021.9561902), Zhou et al., ICRA 2021.

- [RAPTOR: Robust and Perception-Aware Trajectory Replanning for Quadrotor Fast Flight](https://doi.org/10.1109/tro.2021.3071527), Zhou et al., TRO 2021.

- [Dynamic obstacle avoidance for quadrotors with event cameras](https://doi.org/10.1126/scirobotics.aaz9712), Falanga et al., Science Robotics 2020.

- [Robust and Efficient Quadrotor Trajectory Generation for Fast Autonomous Flight](https://doi.org/10.1109/lra.2019.2927938), Zhou et al., RA-L 2019.

- [DroNet: Learning to Fly by Driving](https://doi.org/10.1109/lra.2018.2795643), Loquercio et al., RA-L 2018.

<a id="section-4-2"></a>

### 4.2 Wheeled Robots

Navigation for wheeled mobile robots, covering foundation models, visual and language-conditioned goals, long-range exploration, off-road driving, and socially aware motion planning.

- [From Seeing to Experiencing: Scaling Navigation Foundation Models with Reinforcement Learning](https://proceedings.iclr.cc/paper_files/paper/2026/hash/125be378b39b10676f56e12e6923b902-Abstract-Conference.html), He et al., ICLR 2026.

- [Embodied Navigation Foundation Model](https://proceedings.iclr.cc/paper_files/paper/2026/hash/ceb45c48e29e7f49b0b47edb98e43691-Abstract-Conference.html), Zhang et al., ICLR 2026.

- [NoMaD: Goal Masked Diffusion Policies for Navigation and Exploration](https://doi.org/10.1109/icra57147.2024.10610665), Sridhar et al., ICRA 2024.

- [ViNT: A Foundation Model for Visual Navigation](https://proceedings.mlr.press/v229/shah23a.html), Shah et al., CoRL 2023.

- [GNM: A General Navigation Model to Drive Any Robot](https://doi.org/10.1109/icra48891.2023.10161227), Shah et al., ICRA 2023.

- [FastRLAP: A System for Learning High-Speed Driving via Deep RL and Autonomous Practicing](https://proceedings.mlr.press/v229/stachowicz23a.html), Stachowicz et al., CoRL 2023.

- [Visual Language Maps for Robot Navigation](https://doi.org/10.1109/icra48891.2023.10160969), Huang et al., ICRA 2023.

- [ViKiNG: Vision-Based Kilometer-Scale Navigation with Geographic Hints](https://doi.org/10.15607/rss.2022.xviii.019), Shah et al., RSS 2022.

- [LM-Nav: Robotic Navigation with Large Pre-Trained Models of Language, Vision, and Action](https://proceedings.mlr.press/v205/shah23b.html), Shah et al., CoRL 2022.

- [BADGR: An Autonomous Self-Supervised Learning-Based Navigation System](https://doi.org/10.1109/lra.2021.3057023), Kahn et al., RA-L 2021.

- [ViNG: Learning Open-World Navigation with Visual Goals](https://doi.org/10.1109/icra48506.2021.9561936), Shah et al., ICRA 2021.

- [Socially aware motion planning with deep reinforcement learning](https://doi.org/10.1109/iros.2017.8202312), Chen et al., IROS 2017.

<a id="section-4-3"></a>

### 4.3 Humanoid Robots

Navigation for humanoid robots, including whole-body adaptation, human-to-robot transfer, terrain-aware navigation, footstep planning, and coordinated navigation, locomotion, and reaching.

- [TANGO: Humanoid Navigation in Cluttered Environments with a Whole-Body Vision-Language-Action Model](https://arxiv.org/abs/2609.09158), Li et al., arXiv 2026.

- [Learning Humanoid Navigation From Human Data](https://doi.org/10.1109/lra.2026.3710346), Wang et al., RA-L 2026.

- [Learning Safe Humanoid Navigation from Reduced Order Models](https://arxiv.org/abs/2609.19272), Compton et al., arXiv 2026.

- [GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains](https://arxiv.org/abs/2606.10449), Han et al., arXiv 2026.

- [Hand-Eye Autonomous Delivery: Learning Humanoid Navigation, Locomotion and Reaching](https://proceedings.mlr.press/v305/chen25e.html), Chen et al., CoRL 2025.

- [NaVILA: Legged Robot Vision-Language-Action Model for Navigation](https://doi.org/10.15607/rss.2025.xxi.018), Cheng et al., RSS 2025.

- [Real Time Humanoid Footstep Planning With Foot Angle Difference Consideration for Cost-To-Go Heuristic](https://doi.org/10.1109/ur57808.2023.10202504), Kim et al., UR 2023.

- [Humanoid navigation with dynamic footstep plans](https://doi.org/10.1109/icra.2011.5979656), Garimort et al., ICRA 2011.

<a id="section-4-4"></a>

### 4.4 Quadruped Robots

Navigation and perceptive terrain traversal for quadruped robots, including semantic planning, traversability estimation, parkour, navigation-locomotion coordination, and human guidance.

- [MulDP: Multimodal Diffusion Policy for Autonomous Quadruped Parkour Navigation across Complex Terrains](https://arxiv.org/abs/2609.03984), Hu et al., IROS 2026.

- [Wild visual navigation: fast traversability learning via pre-trained models and online self-supervision](https://doi.org/10.1007/s10514-025-10202-x), Mattamala et al., Autonomous Robots 2025.

- [High-speed control and navigation for quadrupedal robots on complex and discrete terrain](https://doi.org/10.1126/scirobotics.ads6192), Kim et al., Science Robotics 2025.

- [ViPlanner: Visual Semantic Imperative Learning for Local Navigation](https://doi.org/10.1109/icra57147.2024.10610025), Roth et al., ICRA 2024.

- [ANYmal parkour: Learning agile navigation for quadrupedal robots](https://doi.org/10.1126/scirobotics.adi7566), Hoeller et al., Science Robotics 2024.

- [Extreme Parkour with Legged Robots](https://doi.org/10.1109/icra57147.2024.10610200), Cheng et al., ICRA 2024.

- [PIE: Parkour With Implicit-Explicit Learning Framework for Legged Robots](https://doi.org/10.1109/lra.2024.3459797), Luo et al., RA-L 2024.

- [Robot Parkour Learning](https://proceedings.mlr.press/v229/zhuang23a.html), Zhuang et al., CoRL 2023.

- [Seeing-Eye Quadruped Navigation with Force Responsive Locomotion Control](https://proceedings.mlr.press/v229/defazio23a.html), DeFazio et al., CoRL 2023.

- [Learning robust perceptive locomotion for quadrupedal robots in the wild](https://doi.org/10.1126/scirobotics.abk2822), Miki et al., Science Robotics 2022.

- [Learning Vision-Guided Quadrupedal Locomotion End-to-End with Cross-Modal Transformers](https://openreview.net/forum?id=nhnJ3oo6AB), Yang et al., ICLR 2022.

- [Learning a State Representation and Navigation in Cluttered and Dynamic Environments](https://doi.org/10.1109/lra.2021.3068639), Hoeller et al., RA-L 2021.
<a id="section-4-5"></a>

### 4.5 Underwater Robots

Navigation for underwater robots, including dynamics-aware policies, flow sensing, acoustic and visual docking, ecosystem exploration, and visual, inertial, sonar, and depth fusion.

- [AquaWAM: A Dynamics-aware World Action Model for Underwater Embodied Agents](https://arxiv.org/abs/2609.33299), Zhu et al., arXiv 2026.

- [Sensing flow gradients is necessary for learning autonomous underwater navigation](https://doi.org/10.1038/s41467-025-58125-6), Jiao et al., Nature Communications 2025.

- [Position-based acoustic visual servo control for docking of autonomous underwater vehicle using deep reinforcement learning](https://doi.org/10.1016/j.robot.2024.104914), Wang et al., Robotics and Autonomous Systems 2025.

- [Underwater Pose SLAM using GMM scan matching for a mechanical profiling sonar](https://doi.org/10.1002/rob.22272), Vial et al., Journal of Field Robotics 2024.

- [CUREE: A Curious Underwater Robot for Ecosystem Exploration](https://doi.org/10.1109/icra48891.2023.10161282), Girdhar et al., ICRA 2023.

- [SVIn2: A multi-sensor fusion-based underwater SLAM system](https://doi.org/10.1177/02783649221110259), Rahman et al., IJRR 2022.

- [Autonomous Underwater Navigation and Optical Mapping in Unknown Natural Environments](https://doi.org/10.3390/s16081174), Hernández et al., Sensors 2016.

- [Visually Augmented Navigation for Autonomous Underwater Vehicles](https://doi.org/10.1109/joe.2008.923547), Eustice et al., IEEE Journal of Oceanic Engineering 2008.

<a id="section-4-6"></a>

### 4.6 Other and Hybrid Platforms

Navigation for wheeled-legged, aerial-ground, aerial-underwater, snake-like, and surface robots, together with exploration systems combining heterogeneous robot platforms.

- [Image-based Mapless Navigation of a Hybrid Aerial-Underwater Vehicle using Prioritized Deep Reinforcement Learning](https://doi.org/10.1007/s10846-024-02206-z), Costa de Jesus et al., Journal of Intelligent & Robotic Systems 2025.

- [Learning robust autonomous navigation and locomotion for wheeled-legged robots](https://doi.org/10.1126/scirobotics.adi9641), Lee et al., Science Robotics 2024.

- [HE-Nav: A High-Performance and Efficient Navigation System for Aerial-Ground Robots in Cluttered Environments](https://doi.org/10.1109/lra.2024.3468091), Wang et al., RA-L 2024.

- [Multi-Modal Mobility Morphobot (M4) with appendage repurposing for locomotion plasticity enhancement](https://doi.org/10.1038/s41467-023-39018-y), Sihite et al., Nature Communications 2023.

- [CERBERUS: Autonomous Legged and Aerial Robotic Exploration in the Tunnel and Urban Circuits of the DARPA Subterranean Challenge](https://doi.org/10.55417/fr.2022011), Tranzatto et al., Field Robotics 2022.

- [Autonomous Decentralized Shape-Based Navigation for Snake Robots in Dense Environments](https://doi.org/10.1109/icra48506.2021.9561987), Sartoretti et al., ICRA 2021.

- [Roboat II: A Novel Autonomous Surface Vessel for Urban Environments](https://doi.org/10.1109/iros45743.2020.9340712), Wang et al., IROS 2020.

- [Autonomous Hybrid Ground/Aerial Mobility in Unknown Environments](https://doi.org/10.1109/iros40897.2019.8968276), Fan et al., IROS 2019.

<a id="section-5"></a>

## 5. Datasets and Evaluation Benchmarks

<a id="section-5-1"></a>

### 5.1 Odometry, Localization, and Mapping Datasets

Real and synthetic visual, inertial, LiDAR, radar, and event-camera datasets for odometry and SLAM across platforms, motion regimes, and challenging environments.

- [FusionPortableV2: A unified multi-sensor dataset for generalized SLAM across diverse platforms and scalable environments](https://doi.org/10.1177/02783649241303525), Wei et al., IJRR 2025.

- [SubT-MRS Dataset: Pushing SLAM Towards All-weather Environments](https://doi.org/10.1109/cvpr52733.2024.02137), Zhao et al., CVPR 2024.

- [Boreas: A multi-season autonomous driving dataset](https://doi.org/10.1177/02783649231160195), Burnett et al., IJRR 2023.

- [M2DGR: A Multi-Sensor and Multi-Scenario SLAM Dataset for Ground Robots](https://doi.org/10.1109/lra.2021.3138527), Yin et al., RA-L 2022.

- [The Hilti SLAM Challenge Dataset](https://doi.org/10.1109/lra.2022.3183759), Helmberger et al., RA-L 2022.

- [TartanAir: A Dataset to Push the Limits of Visual SLAM](https://doi.org/10.1109/iros45743.2020.9341801), Wang et al., IROS 2020.

- [The Oxford Radar RobotCar Dataset: A Radar Extension to the Oxford RobotCar Dataset](https://doi.org/10.1109/icra40945.2020.9196884), Barnes et al., ICRA 2020.

- [Are We Ready for Autonomous Drone Racing? The UZH-FPV Drone Racing Dataset](https://doi.org/10.1109/icra.2019.8793887), Delmerico et al., ICRA 2019.

- [The TUM VI Benchmark for Evaluating Visual-Inertial Odometry](https://doi.org/10.1109/iros.2018.8593419), Schubert et al., IROS 2018.

- [The event-camera dataset and simulator: Event-based data for pose estimation, visual odometry, and SLAM](https://doi.org/10.1177/0278364917691115), Mueggler et al., IJRR 2017.

- [The EuRoC micro aerial vehicle datasets](https://doi.org/10.1177/0278364915620033), Burri et al., IJRR 2016.

- [Vision meets robotics: The KITTI dataset](https://doi.org/10.1177/0278364913491297), Geiger et al., IJRR 2013.

<a id="section-5-2"></a>

### 5.2 Navigation Task Datasets and Benchmarks

Simulation platforms and scene resources, together with visual-goal, semantic-goal, language-guided, audio-visual, lifelong, and aerial navigation benchmarks.

- [GOAT-Bench: A Benchmark for Multi-Modal Lifelong Navigation](https://doi.org/10.1109/cvpr52733.2024.01549), Khanna et al., CVPR 2024.

- [HM3D-OVON: A Dataset and Benchmark for Open-Vocabulary Object Goal Navigation](https://doi.org/10.1109/iros58592.2024.10802709), Yokoyama et al., IROS 2024.

- [AerialVLN: Vision-and-Language Navigation for UAVs](https://doi.org/10.1109/iccv51070.2023.01411), Liu et al., ICCV 2023.

- [ProcTHOR: Large-Scale Embodied AI Using Procedural Generation](https://doi.org/10.52202/068431-0433), Deitke et al., NeurIPS 2022.

- [Habitat-Matterport 3D Dataset (HM3D): 1000 Large-scale 3D Environments for Embodied AI](https://datasets-benchmarks-proceedings.neurips.cc/paper_files/paper/2021/hash/34173cb38f07f89ddbebc2ac9128303f-Abstract-round2.html), Ramakrishnan et al., NeurIPS Datasets and Benchmarks 2021.

- [Beyond the Nav-Graph: Vision-and-Language Navigation in Continuous Environments](https://doi.org/10.1007/978-3-030-58604-1_7), Krantz et al., ECCV 2020.

- [REVERIE: Remote Embodied Visual Referring Expression in Real Indoor Environments](https://doi.org/10.1109/cvpr42600.2020.01000), Qi et al., CVPR 2020.

- [RoboTHOR: An Open Simulation-to-Real Embodied AI Platform](https://doi.org/10.1109/cvpr42600.2020.00323), Deitke et al., CVPR 2020.

- [Room-Across-Room: Multilingual Vision-and-Language Navigation with Dense Spatiotemporal Grounding](https://doi.org/10.18653/v1/2020.emnlp-main.356), Ku et al., EMNLP 2020.

- [SoundSpaces: Audio-Visual Navigation in 3D Environments](https://doi.org/10.1007/978-3-030-58539-6_2), Chen et al., ECCV 2020.

- [Habitat: A Platform for Embodied AI Research](https://doi.org/10.1109/iccv.2019.00943), Savva et al., ICCV 2019.

- [Vision-and-Language Navigation: Interpreting Visually-Grounded Navigation Instructions in Real Environments](https://doi.org/10.1109/cvpr.2018.00387), Anderson et al., CVPR 2018.

<a id="section-5-3"></a>

### 5.3 Real-Robot and Cross-Platform Data

Real-world robot and human navigation data, datasets spanning robot platforms, social navigation demonstrations, and off-road perception and driving data.

- [ACME: A Multi-Cultural, Multi-Embodiment Social-Navigation Dataset](https://arxiv.org/abs/2607.21964), Marpally et al., arXiv 2026.

- [NaviTrace: Evaluating Embodied Navigation of Vision-Language Models](https://doi.org/10.1109/icra57385.2026.11697251), Windecker et al., ICRA 2026.

- [WildScenes: A benchmark for 2D and 3D semantic segmentation in large-scale natural environments](https://doi.org/10.1177/02783649241278369), Vidanapathirana et al., IJRR 2025.

- [TartanDrive 2.0: More Modalities and Better Infrastructure to Further Self-Supervised Learning Research in Off-Road Driving Tasks](https://doi.org/10.1109/icra57147.2024.10611265), Sivaprakasam et al., ICRA 2024.

- [GNM: A General Navigation Model to Drive Any Robot](https://doi.org/10.1109/icra48891.2023.10161227), Shah et al., ICRA 2023.

- [JRDB: A Dataset and Benchmark of Egocentric Robot Visual Perception of Humans in Built Environments](https://doi.org/10.1109/tpami.2021.3070543), Martín-Martín et al., TPAMI 2023.

- [Toward Human-Like Social Robot Navigation: A Large-Scale, Multi-Modal, Social Human Navigation Dataset](https://doi.org/10.1109/iros55552.2023.10342447), Nguyen et al., IROS 2023.

- [Socially CompliAnt Navigation Dataset (SCAND): A Large-Scale Dataset of Demonstrations for Social Navigation](https://doi.org/10.1109/lra.2022.3184025), Karnan et al., RA-L 2022.

- [RELLIS-3D Dataset: Data, Benchmarks and Analysis](https://doi.org/10.1109/icra48506.2021.9561251), Jiang et al., ICRA 2021.

- [A RUGD Dataset for Autonomous Navigation and Visual Perception in Unstructured Outdoor Environments](https://doi.org/10.1109/iros40897.2019.8968283), Wigness et al., IROS 2019.

<a id="section-5-4"></a>

### 5.4 Evaluation Metrics and Experimental Protocols

Navigation success and path efficiency, instruction fidelity, trajectory error, and evaluation protocols for social navigation and robustness.

- [SocNavBench: A Grounded Simulation Testing Framework for Evaluating Social Navigation](https://doi.org/10.1145/3476413), Biswas et al., ACM THRI 2022.

- [RobustNav: Towards Benchmarking Robustness in Embodied Navigation](https://doi.org/10.1109/iccv48922.2021.01540), Chattopadhyay et al., ICCV 2021.

- [General Evaluation for Instruction Conditioned Navigation using Dynamic Time Warping](https://vigilworkshop.github.io/static/papers-2019/33.pdf), Ilharco et al., NeurIPS ViGIL Workshop 2019.

- [Stay on the Path: Instruction Fidelity in Vision-and-Language Navigation](https://doi.org/10.18653/v1/p19-1181), Jain et al., ACL 2019.

- [A Tutorial on Quantitative Trajectory Evaluation for Visual(-Inertial) Odometry](https://doi.org/10.1109/iros.2018.8593941), Zhang et al., IROS 2018.

- [On Evaluation of Embodied Navigation Agents](https://arxiv.org/abs/1807.06757), Anderson et al., arXiv 2018.

- [A benchmark for the evaluation of RGB-D SLAM systems](https://doi.org/10.1109/iros.2012.6385773), Sturm et al., IROS 2012.

- [On measuring the accuracy of SLAM algorithms](https://doi.org/10.1007/s10514-009-9155-6), Kümmerle et al., Autonomous Robots 2009.

<a id="section-5-5"></a>

### 5.5 Competitions and Leaderboards

Official competition and leaderboard resources for embodied navigation, aerial language-guided navigation, constrained-space navigation, SLAM, autonomous driving, and racing.

- [Habitat Navigation Challenge 2023](https://aihabitat.org/challenge/2023/), Habitat Team. Archived official challenge page, 2023 edition.

- [Vision and Language Navigation Leaderboard](https://eval.ai/web/challenges/challenge-page/97/overview), VLN Team. Official leaderboard.

- [RxR Competition](https://ai.google.com/research/rxr/competition?active_tab=leaderboard), Google Research. Official leaderboard.

- [Aerial Vision-and-Language Navigation Challenge](https://eval.ai/web/challenges/challenge-page/2049/leaderboard), UCSC ERIC Lab. Archived official leaderboard.

- [The BARN Challenge 2026](https://people.cs.gmu.edu/~xiao/Research/BARN_Challenge/BARN_Challenge26.html), BARN Challenge Organizers. Official ICRA 2026 challenge and results.

- [Hilti × Trimble SLAM Challenge 2026](https://hilti-trimble-challenge.com/), Hilti, Trimble, and the University of Oxford. Official 2026 challenge and evaluation portal.

- [CARLA Autonomous Driving Leaderboard](https://leaderboard.carla.org/), CARLA Team. Official leaderboard and evaluation protocol.

- [31st RoboRacer Autonomous Racing Competition](https://iros2026-race.roboracer.ai/), RoboRacer Organizers. Official IROS 2026 competition page.
