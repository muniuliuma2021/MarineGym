![Visualization of MarineGym](docs/overview.png)

---

# MarineGym

[![IsaacSim](https://img.shields.io/badge/Isaac%20Sim-4.1.0-orange.svg)](https://docs.isaacsim.omniverse.nvidia.com/4.2.0/archived_release_notes.html)
[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://docs.python.org/3/whatsnew/3.7.html)
[![CI](https://github.com/muniuliuma2021/MarineGym/actions/workflows/ci.yml/badge.svg)](https://github.com/muniuliuma2021/MarineGym/actions/workflows/ci.yml)
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

## Acknowledgement

The architecture and certain implementation ideas build upon concepts introduced in [OmniDrones](https://github.com/btx0424/OmniDrones).

---

## 编译与部署说明（中文）

### 环境要求

| 依赖项 | 版本要求 |
|--------|---------|
| 操作系统 | Ubuntu 20.04 / 22.04 / 24.04 |
| Python | 3.10 |
| NVIDIA Isaac Sim | 4.1.0 |
| PyTorch | 2.2.2 |
| CUDA（完整功能） | 11.8 或 12.x |

> **注意**：Isaac Sim 需要支持 CUDA 的 NVIDIA GPU（RTX 3070 或更高）。
> 如需在无 GPU 的环境（如 CI 流水线）中运行基础功能测试，可跳过 Isaac Sim 的安装。

---

### 一、完整安装（含 Isaac Sim）

#### 1. 安装 Isaac Sim

按照 [NVIDIA Isaac Sim 官方安装指南](https://docs.isaacsim.omniverse.nvidia.com/) 安装 Isaac Sim 4.1.0。
安装完成后，记录 Isaac Sim 的安装路径（默认为 `~/.local/share/ov/pkg/isaac_sim-4.1.0`）。

#### 2. 创建并配置 Conda 环境

```bash
# 创建 Python 3.10 的 conda 环境
conda create -n marinegym python=3.10
conda activate marinegym

# 设置 Isaac Sim 路径（替换为你的实际安装路径）
export ISAACSIM_PATH=~/.local/share/ov/pkg/isaac_sim-4.1.0
export ISAACSIM_PYTHON_EXE=${ISAACSIM_PATH}/python.sh

# 将 conda 激活/停用脚本复制到环境中
cp -r conda_setup/etc $CONDA_PREFIX/
```

#### 3. 安装 Python 依赖

```bash
# 激活 Isaac Sim 的 Conda 环境变量
source ${ISAACSIM_PATH}/setup_conda_env.sh

# 安装 PyTorch（与 Isaac Sim 兼容的版本）
pip install torch==2.2.2 torchvision==0.17.2 --index-url https://download.pytorch.org/whl/cu118

# 安装 torchrl 和 tensordict（需与 PyTorch 版本对应）
pip install torchrl==0.4.0 tensordict==0.4.0

# 安装项目其他依赖
pip install hydra-core omegaconf wandb imageio plotly einops pandas moviepy av setproctitle
```

#### 4. 安装 MarineGym

```bash
# 克隆代码仓库
git clone https://github.com/muniuliuma2021/MarineGym.git
cd MarineGym

# 以可编辑模式安装（开发推荐）
pip install -e .
```

#### 5. 验证安装

```bash
# 验证 Isaac Sim 集成
python -c "from isaacsim import SimulationApp; print('Isaac Sim 安装成功')"

# 验证 MarineGym
python -c "import torch; import torchrl; print('依赖安装成功')"
```

---

### 二、CI 环境安装（无 Isaac Sim，适用于 Ubuntu 24.04）

在无 GPU 的 CI/CD 环境（如 GitHub Actions）中，可以安装不依赖 Isaac Sim 的版本来运行基础功能测试。

#### 1. 设置 Python 3.10

```bash
# Ubuntu 24.04 默认 Python 为 3.12，需额外安装 3.10
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-dev

# 创建虚拟环境
python3.10 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

#### 2. 安装 CI 依赖

```bash
# 安装 CPU 版 PyTorch（CI 环境无需 GPU）
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cpu

# 安装 torchrl 和 tensordict（CI 兼容版本）
pip install torchrl==0.5.0 tensordict==0.5.0

# 安装其他依赖
pip install hydra-core omegaconf wandb imageio plotly einops pandas moviepy av setproctitle pytest
```

#### 3. 安装 MarineGym（跳过版本约束检查）

```bash
git clone https://github.com/muniuliuma2021/MarineGym.git
cd MarineGym
pip install -e . --no-deps
```

#### 4. 运行基础测试

```bash
python -m pytest tests/ -v
```

---

### 三、训练流程

安装完成后，进入 `scripts` 目录启动训练：

```bash
cd scripts

# 启动悬停任务训练（有显示界面）
python train.py task=Hover algo=ppo headless=false enable_livestream=false

# 无头模式训练（推荐用于服务器/Docker 环境）
python train.py task=Hover algo=ppo headless=true enable_livestream=false

# 可用任务：Hover（悬停）、Track（轨迹跟踪）、Landing（着陆）
python train.py task=Track algo=ppo headless=true enable_livestream=false
python train.py task=Landing algo=ppo headless=true enable_livestream=false
```

训练日志与模型检查点默认保存在 `outputs/` 目录下。如需可视化训练曲线，可在启动前配置 `wandb`：

```bash
wandb login  # 输入你的 W&B API Key
```

---

### 四、Docker 部署

如需在 Docker 容器中部署（推荐用于无桌面的训练服务器），请参考
[Docker 环境安装指南](https://marinegym.netlify.app/docker_environment)。

---

### 五、常见问题

- **`ModuleNotFoundError: No module named 'isaacsim'`**：Isaac Sim 未安装或环境变量未正确设置，请确认已执行 `source ${ISAACSIM_PATH}/setup_conda_env.sh`。
- **CUDA 版本不匹配**：请确认 PyTorch 安装时使用的 CUDA 版本与系统驱动版本一致。
- **torchrl/tensordict 版本冲突**：CI 环境使用 `torchrl==0.5.0` / `tensordict==0.5.0`，完整运行环境使用 `torchrl==0.4.0` / `tensordict==0.4.0`（需配合 `torch==2.2.2`）。
- 更多问题请查阅 [FAQ](https://marinegym.netlify.app/faq) 或提交 Issue。

