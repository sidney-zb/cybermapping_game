import numpy as np
from matplotlib import pylab as plt


# 递归计算攻击方（端口关闭情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_left(c, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
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
                + (1 - xt) * (ADpayoff_left(c, n, pe * (1 - xt), round + 1))
            )
            + (1 - pe) * vh
        )
        return AD_l
    else:
        AD_l = pe * (
            xt * ((t**round) * vh - (round + 1) * c)
            + (1 - xt) * (ADpayoff_left(c, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (-(t ** (round - 1)) * vh - round * c)
        return AD_l


# 递归计算攻击方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_right(c, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
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
        AD_r = pe * 1 * (ADpayoff_right(c, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            vl - round * c
        )
        return AD_r
    else:
        AD_r = pe * 1 * (ADpayoff_right(c, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            (t ** (round - 1)) * vl - round * c
        )
        return AD_r


def ADpayoff(c, n, pe, round):
    return ADpayoff_right(c, n, pe, round) + ADpayoff_left(c, n, pe, round)


# 生成x轴数据
c = np.linspace(1, 10, 100)
# 计算函数值
ua = ADpayoff(c, 10, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(c, ua, label="1experiment")
plt.title("Function Plot")
plt.xlabel("c")
plt.ylabel("Ua")
plt.legend()
plt.grid(True)
plt.savefig("c-ua.png")  # 可以保存为其他格式，如PDF
