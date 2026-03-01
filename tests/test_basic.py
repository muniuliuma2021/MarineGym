"""
MarineGym 基础功能测试（不依赖 Isaac Sim）
这些测试验证数学工具函数的正确性，可在标准 CI 环境中运行。
"""

import math
import torch
import pytest


def test_torch_available():
    """验证 PyTorch 可用"""
    assert torch.__version__ is not None
    t = torch.tensor([1.0, 2.0, 3.0])
    assert t.sum().item() == 6.0


def test_quaternion_to_rotation_matrix():
    """测试四元数转旋转矩阵"""
    from marinegym.utils.math import quaternion_to_rotation_matrix

    # 单位四元数应给出单位矩阵
    q = torch.tensor([1.0, 0.0, 0.0, 0.0])
    R = quaternion_to_rotation_matrix(q)
    assert R.shape == (3, 3)
    assert torch.allclose(R, torch.eye(3), atol=1e-6)


def test_quaternion_to_euler():
    """测试四元数转欧拉角"""
    from marinegym.utils.math import quaternion_to_euler

    # 单位四元数应给出零欧拉角
    q = torch.tensor([1.0, 0.0, 0.0, 0.0])
    euler = quaternion_to_euler(q)
    assert euler.shape == (3,)
    assert torch.allclose(euler, torch.zeros(3), atol=1e-6)


def test_euler_to_quaternion():
    """测试欧拉角转四元数"""
    from marinegym.utils.math import euler_to_quaternion

    # 零欧拉角应给出单位四元数
    euler = torch.tensor([0.0, 0.0, 0.0])
    q = euler_to_quaternion(euler)
    assert q.shape == (4,)
    expected = torch.tensor([1.0, 0.0, 0.0, 0.0])
    assert torch.allclose(q, expected, atol=1e-6)


def test_euler_quaternion_roundtrip():
    """测试欧拉角 -> 四元数 -> 欧拉角的往返转换"""
    from marinegym.utils.math import euler_to_quaternion, quaternion_to_euler

    euler_in = torch.tensor([0.1, 0.2, 0.3])
    q = euler_to_quaternion(euler_in)
    euler_out = quaternion_to_euler(q)
    assert torch.allclose(euler_in, euler_out, atol=1e-5)


def test_normalize():
    """测试向量归一化"""
    from marinegym.utils.math import normalize

    v = torch.tensor([3.0, 4.0, 0.0])
    n = normalize(v)
    assert abs(torch.norm(n).item() - 1.0) < 1e-6


def test_dependencies_importable():
    """验证所有非 Isaac Sim 依赖均可正常导入"""
    import hydra          # noqa: F401
    import omegaconf      # noqa: F401
    import einops         # noqa: F401
    import pandas         # noqa: F401
    import plotly         # noqa: F401
    import tensordict     # noqa: F401
    import torchrl        # noqa: F401
