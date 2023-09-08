import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 递归计算攻击方（端口关闭情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_left(xt, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
    c = 1
    # 端口不响应成本
    x = 2
    # 攻击方耐心
    t = 1
    # 自然选择概率
    p = 0.5

    # 递归轮次

    # 耐心随轮次指数增长
    # 递归结束条件
    if round == n:
        AD_l = pe * (
            xt * ((t**n) * vh - (n + 1) * c)
            + (1 - xt) * (-(t**n) * vh - (n + 1) * c)
        ) + (1 - pe) * (-(t ** (n - 1)) * vh - n * c)
        return AD_l
    elif round == 0:
        AD_l = (
            pe
            * (
                xt * (vh - (round + 1) * c)
                + (1 - xt) * (ADpayoff_left(xt, n, pe * (1 - xt), round + 1))
            )
            + (1 - pe) * vh
        )
        return AD_l
    else:
        AD_l = pe * (
            xt * ((t**round) * vh - (round + 1) * c)
            + (1 - xt) * (ADpayoff_left(xt, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (-(t ** (round - 1)) * vh - round * c)
        return AD_l


# 递归计算攻击方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_right(xt, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
    c = 1
    # 端口不响应成本
    x = 2
    # 攻击方耐心
    t = 1
    # 自然选择概率
    p = 0.5
    # 递归轮次

    # 耐心随轮次指数增长
    # 递归结束条件
    if round == n:
        AD_r = pe * 1 * ((t**n) * (vl) - (n + 1) * c) + (1 - pe) * (
            (t ** (n - 1)) * vl - n * c
        )
        return AD_r
    elif round == 0:
        AD_r = pe * 1 * (ADpayoff_right(xt, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            vl - round * c
        )
        return AD_r
    else:
        AD_r = pe * 1 * (ADpayoff_right(xt, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            (t ** (round - 1)) * vl - round * c
        )
        return AD_r


def ADpayoff(xt, n, pe, round):
    return ADpayoff_right(xt, n, pe, round) + ADpayoff_left(xt, n, pe, round)


# 创建变量范围
xt_values = np.linspace(0, 1, 100)  # 变量 xt 的范围
n_values = np.arange(1, 10)  # 变量 n 的范围

# 创建网格
X, Y = np.meshgrid(xt_values, n_values)

# 计算函数的值
AD_values = np.empty_like(X)

for i in range(len(n_values)):
    for j in range(len(xt_values)):
        AD_values[i, j] = ADpayoff(X[i, j], Y[i, j], 0.8, 0)

# 绘制三维曲面图
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

# 绘制曲面
ax.plot_surface(X, Y, AD_values, cmap="viridis")

# 添加标签
ax.set_xlabel("xt")
ax.set_ylabel("n")
ax.set_zlabel("ADpayoff")
ax.set_title("ADpayoff as a 3D Function of xt and n")

# 显示图形
plt.show()
