import numpy as np
from matplotlib import pylab as plt

# 创建一个3D图形窗口
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# 创建 x 和 y 值的网格，指定原点位置
vh = np.linspace(1, 10, 100)
vl = np.linspace(1, 10, 100)
H, L = np.meshgrid(vh, vl)


def ADpayoff_left(vh, vl, n, pe, round):
    # 博弈初始配置
    # 端口开放
    # 端口关闭
    # 测绘成本
    c = 1
    # 端口不响应成本
    x = 4
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
                + (1 - xt) * (ADpayoff_left(vh, vl, n, pe * (1 - xt), round + 1))
            )
            + (1 - pe) * vh
        )
        return AD_l
    else:
        AD_l = pe * (
            xt * ((t**round) * vh - (round + 1) * c)
            + (1 - xt) * (ADpayoff_left(vh, vl, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (-(t ** (round - 1)) * vh - round * c)
        return AD_l


# 递归计算攻击方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_right(vh, vl, n, pe, round):
    # 博弈初始配置
    # 端口开放

    # 端口关闭

    # 测绘成本
    c = 1
    # 端口不响应成本
    x = 4
    # 攻击方耐心
    t = 1
    # 自然选择概率
    p = 0.5
    # 西塔
    xt = 0.23
    # 递归轮次

    # 耐心随轮次指数增长
    # 递归结束条件
    if round == n:
        AD_r = pe * 1 * ((t**n) * (vl) - (n + 1) * c) + (1 - pe) * (
            (t ** (n - 1)) * vl - n * c
        )
        return AD_r
    elif round == 0:
        AD_r = pe * 1 * (ADpayoff_right(vh, vl, n, pe * (1 - xt), round + 1)) + (
            1 - pe
        ) * (vl - round * c)
        return AD_r
    else:
        AD_r = pe * 1 * (ADpayoff_right(vh, vl, n, pe * (1 - xt), round + 1)) + (
            1 - pe
        ) * ((t ** (round - 1)) * vl - round * c)
        return AD_r


def ADpayoff(vh, vl, n, pe, round):
    return ADpayoff_right(vh, vl, n, pe, round) + ADpayoff_left(vh, vl, n, pe, round)


# 定义二元函数，这里以一个简单的二元正弦函数为例
Z = ADpayoff(H, L, 8, 0.5, 0)

# 绘制3D曲面图
ax.plot_surface(H, L, Z, cmap="viridis")

# 添加轴标签
ax.set_xlabel("H轴")
ax.set_ylabel("L轴")
ax.set_zlabel("Z轴")

# 显示图形
plt.show()
