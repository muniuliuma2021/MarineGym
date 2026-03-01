![Visualization of MarineGym](docs/overview.png)

---

# MarineGym

[![IsaacSim](https://img.shields.io/badge/Isaac%20Sim-4.1.0-orange.svg)](https://docs.isaacsim.omniverse.nvidia.com/4.2.0/archived_release_notes.html)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.7.html)
[![Docs](https://img.shields.io/badge/docs-passing-brightgreen)](https://marinegym.netlify.app/)
[![Website](https://img.shields.io/website?url=https%3A%2F%2Fmarine-gym.com&label=website&up_message=online&down_message=offline)](https://marine-gym.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

*MarineGym* is a large-scale parallel framework designed for reinforcement learning research on unmanned underwater vehicles (UUVs). It is built upon [OmniDrones](https://github.com/btx0424/OmniDrones) and [Isaac Sim](https://developer.nvidia.com/isaac/sim), offering the following features:

- Efficiency: Achieve a simulation speed of up to 10<sup>7</sup> steps per second.
- Fidelity: Accurately replicate the physical environment, including physical laws, kinematics, and dynamics.
- Flexibility:  Ensure compatibility with existing RL frameworks and offer user-friendly APIs to facilitate seamless integration and usage.
- Evaluation: Assesses and contrasts various RL strategies through multiple tasks.

## Installation

To install MarineGym, we recommend reading one of the following guides:
- [Installation from Source](https://marinegym.netlify.app/installation_from_source) (recommended for development)
- [Docker Environment](https://marinegym.netlify.app/docker_environment) (recommended for training purposes; no visualization interface)

If you encounter any issues, you can find solutions to common problems in the [FAQ](https://marinegym.netlify.app/faq) or feel free to open an issue.

For training and evaluation commands, please take a look at the [Quick Start](https://marinegym.netlify.app/quick_start).

## Usage
For installation details, please refer to our [Setup Guide](https://marinegym.netlify.app/installation_from_source/).

Currently, five gym environments are verified: Hover, Circle Tracking, Helical Tracking, Lemniscate Tracking, and Landing. Additional environments, including vision-based and sonar-based tasks, are under development.

The training script is located in the `scripts` folder, named `train.py`.


To start the training process, run:

```bash
python train.py task=Hover algo=ppo headless=false enable_livestream=false
```
where `task` specifies the training scenario, which can be `Hover`, `Track`, or `Landing`.


## Citation

If you build on this work, please cite our paper:

```bibtex
@online{chu_2025_MarineGymHighPerformanceReinforcement,
        title = {MarineGym: A High-Performance Reinforcement Learning Platform for Underwater Robotics},
        shorttitle = {MarineGym},
        author = {Chu, Shuguang and Huang, Zebin and Li, Yutong and Lin, Mingwei and Carlucho, Ignacio and Petillot, Yvan R. and Yang, Canjun},
        date = {2025-03-12},
        eprint = {2503.09203},
        eprinttype = {arXiv},
        eprintclass = {cs},
        doi = {10.48550/arXiv.2503.09203},
        pubstate = {prepublished}
        }
```

## Platform & Requirements

MarineGym is **not ROS-based**. It is built directly on top of [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) (an Omniverse-based robotics simulation platform) and [OmniDrones](https://github.com/btx0424/OmniDrones). No ROS installation is required.

**Hardware & OS requirements:**

| Requirement | Details |
|---|---|
| Operating System | Ubuntu 22.04 (Linux) |
| GPU | NVIDIA RTX series (RTX 3080 or better recommended) |
| CUDA | 12.1+ |
| RAM | 32 GB+ |

**Software requirements:**

| Requirement | Version |
|---|---|
| [NVIDIA Isaac Sim](https://developer.nvidia.com/isaac/sim) | 4.1.0 |
| Python | 3.10 |
| PyTorch | 2.2.2 |

## Roadmap

The following environments have been verified and are ready to use:

- **Hover** – stabilize the UUV at a target position
- **Circle Tracking** – follow a circular trajectory
- **Helical Tracking** – follow a helical trajectory
- **Lemniscate Tracking** – follow a figure-8 trajectory
- **Landing** – dock the UUV on a landing pad

The following environments are currently **under development**:

- Vision-based navigation tasks (using onboard camera)
- Sonar-based perception tasks (using acoustic sensors)

Contributions are welcome! See [Issues](https://github.com/muniuliuma2021/MarineGym/issues) for open tasks.

## FAQ

**Q: Does MarineGym require ROS?**
No. MarineGym runs entirely on NVIDIA Isaac Sim and does not depend on ROS (Robot Operating System). If you need ROS integration for deployment on a real UUV, you would need to add a ROS bridge on top of the trained policy, but this is not part of MarineGym itself.

**Q: What GPU do I need?**
An NVIDIA RTX GPU is required. We recommend at least an RTX 3080 (10 GB VRAM) for comfortable training. Higher-end GPUs (e.g., RTX 4090 or A100) will significantly increase simulation throughput.

**Q: Can I run MarineGym in Docker without a display?**
Yes. The [Docker Environment](https://marinegym.netlify.app/docker_environment) guide covers headless training without a visual interface.

**Q: What RL algorithms are supported?**
MarineGym is compatible with standard RL frameworks. The example training script uses PPO. You can integrate any algorithm that works with the Gym-style API.

## Acknowledgement

The architecture and certain implementation ideas build upon concepts introduced in [OmniDrones](https://github.com/btx0424/OmniDrones).
