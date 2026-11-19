# An Intelligent Roadside Unit for AI-Based Pedestrian Traffic Risk Detection and V2X Warning Generation

**Master's Thesis — Halmstad University, Sweden**

**Authors:** Joxy John and Sreelakshmi Cheruvayippil Babu  
**Academic Advisor:** Alexandre dos Santos Roque  
**Institution:** Halmstad University

## Project Overview

This master's thesis investigates an AI-based Intelligent Interactive Roadside Unit (I2RSU) for assessing pedestrian safety at crosswalks. The proposed approach combines YOLOv8n object detection, scene-level feature extraction, rule-based safety labeling, Random Forest safety classification, and vehicle-facing analysis to estimate pedestrian–vehicle risk.

The experiments use traffic imagery, SUMO simulations, and a miniature crosswalk environment. A SunFounder PiCar-X equipped with a Raspberry Pi 5 and a camera serves as a stationary prototype. Safety conditions are displayed through the developed xWalk graphical user interface.

MQTT provides preliminary application-level wireless communication validation. It does not represent standardized V2X communication. Future research may extend the system using dedicated V2X hardware.

## Software and Research Components

| Component | Purpose |
|---|---|
| YOLOv8n | Detect pedestrians, vehicles, and crosswalk-related objects |
| Scene-level feature extraction | Describe pedestrian–vehicle interactions at crossings |
| Rule-based labeling and Random Forest | Estimate SAFE, WARNING, and DANGER conditions |
| Vehicle-facing classifier | Refine safety predictions using vehicle orientation |
| SUMO | Generate and evaluate simulated traffic scenarios |
| PiCar-X / Raspberry Pi 5 | Prototype hardware and camera-based observation |
| xWalk GUI and MQTT | Display predictions and evaluate preliminary communication |

## GitHub Project Repositories

The TARS organization contains two public integration repositories.

**1. [xWalkPiCarAI](https://github.com/TARS-v00-01/xWalkPiCarAI)**

Raspberry Pi 5 and PiCar-X integration, C++ control software, hardware interfaces, simulation backends, and related documentation.

**2. [xWalkPiCarApp](https://github.com/TARS-v00-01/xWalkPiCarApp)**

AI model-training integration, Python desktop GUI, application integration, and development tools.

**Access Note:** These public integration repositories currently reference some private Git submodules. Public access to the integration repositories does not automatically provide access to every component's source code. Future students can request authorised access to restricted components through the organisation.

## Dataset — Hugging Face

The datasets used for model training and evaluation are hosted separately on Hugging Face due to their large size.

**Dataset Repository:** [xWalkTrafficDataset on Hugging Face](https://huggingface.co/datasets/joxjoh24/xWalkTrafficDataset)

The dataset is available for future research and further development of the proposed I2RSU framework.

## Master's Thesis

The complete master's thesis describes the research objectives, system architecture, methodology, AI model development, experimental validation, results, limitations, and future research directions.

**Thesis PDF:** Link will be added after publication.

## Guide for Future Students

1. Read the master's thesis to understand the system architecture, methodology, experimental results, and limitations.
2. Explore the GitHub repositories and their individual README files.
3. Access the datasets through the Hugging Face repository.
4. Follow the installation and setup instructions provided in the respective GitHub repositories.
5. Request access to restricted components if required.
6. Extend the proposed system through improved AI perception, additional real-world testing, and dedicated V2X hardware integration.

## Organization Membership and Contributions

Students and researchers interested in continuing this project may request access to the organisation's restricted repositories.

**[Request Membership](https://github.com/TARS-v00-01/.github/issues/new?template=membership-request.yml)**

Membership requests are reviewed by the organisation owners. Approved membership may provide read access to private repositories but does not automatically grant permission to modify them.

For more information, see the [Contribution Guidelines](https://github.com/TARS-v00-01/.github/blob/master/CONTRIBUTING.md).

## Research Continuity and Future Work

This GitHub organisation and the associated Hugging Face dataset provide resources for future students and researchers interested in extending the proposed I2RSU framework.

Future research may investigate improved detection accuracy, temporal safety prediction, more diverse traffic environments, and practical validation using dedicated V2X communication hardware, such as C-V2X or ITS-G5.

The objective of making these resources available is to support future research, reproducibility, and continued development of AI-based pedestrian safety assessment systems.
