import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义函数 UD1payoff
def UD1payoff(xt, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
    c = 2
    # 端口不响应成本
    x = 4
    # 攻击方耐心
    t = 1
    # 自然选择概率
    p = 0.5
    # 西塔
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
            + (1 - xt) * (UD1payoff(xt, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (vh + round * c - round * x)
        return UD1
    else:
        UD1 = pe * (
            xt * (-(t**round) * vh + (round + 1) * c - (round * x))
            + (1 - xt) * (UD1payoff(xt, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * ((t ** (round - 1)) * vh + round * c - round * x)

        return UD1


# 创建变量范围
xt_values = np.linspace(0, 1, 100)  # 变量 xt 的范围
n_values = np.arange(1, 20)  # 变量 n 的范围

# 创建网格
X, Y = np.meshgrid(xt_values, n_values)

# 计算函数的值
UD1_values = np.empty_like(X)

for i in range(len(n_values)):
    for j in range(len(xt_values)):
        UD1_values[i, j] = UD1payoff(X[i, j], Y[i, j], 0.8, 0)

# 绘制三维曲面图
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

# 绘制曲面
ax.plot_surface(X, Y, UD1_values, cmap="viridis")

# 添加标签
ax.set_xlabel("xt")
ax.set_ylabel("n")
ax.set_zlabel("UD1payoff")
ax.set_title("UD1payoff as a 3D Function of xt and n")

# 显示图形
plt.show()
