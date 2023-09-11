import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 创建一个3D图形窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# 创建 x 和 y 值的网格，指定原点位置
x = np.linspace(1, 10, 100)
c = np.linspace(1, 10, 100)
X, Y = np.meshgrid(x, c)


def UD1payoff(x, c, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本

    # 端口不响应成本

    # 攻击方耐心
    t = 1
    # 自然选择概率
    p = 0.5
    # 西塔
    xt = 0.5
    # 递归轮次

    # 耐心随轮次指数增长
    # 递归结束条件
    if round == n:
        UD1 = pe * (
            xt * (-(t**n) * vh + (n + 1) * c - (n * x))
            + (1 - xt) * ((t**n) * vh + (n + 1) * c - (n - 1) * x)
        ) + (1 - pe) * ((t ** (n - 1)) * vh + n * c - n * x)

        return UD1
    elif round == 0:
        UD1 = pe * (
            xt * (-(t**round) * vh + (round + 1) * c - (round * x))
            + (1 - xt) * (UD1payoff(x, c, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (vh + round * c - round * x)
        return UD1
    else:
        UD1 = pe * (
            xt * (-(t**round) * vh + (round + 1) * c - (round * x))
            + (1 - xt) * (UD1payoff(x, c, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * ((t ** (round - 1)) * vh + round * c - round * x)

        return UD1


# 定义二元函数，这里以一个简单的二元正弦函数为例
Z = UD1payoff(X, Y, 10, 0.5, 0)

# 绘制3D曲面图
ax.plot_surface(X, Y, Z, cmap="viridis")

# 添加轴标签
ax.set_xlabel("X轴")
ax.set_ylabel("c轴")
ax.set_zlabel("ud1轴")

# 显示图形
plt.show()
