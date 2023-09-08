import numpy as np
from matplotlib import pylab as plt


# 定义函数θ-ud1，θ为变量
# 递归计算防御方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def UD1payoff(xt, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
    c = 1
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
            + (1 - xt) * ((t**n) * vh + (n + 1) * c - (n + 1) * x)
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


# 生成x轴数据
xt = np.linspace(0, 1, 100)
# 计算函数值
y1 = UD1payoff(xt, 10, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, y1, label="1experiment")
plt.title("Function Plot")
plt.xlabel("θ")
plt.ylabel("Ud1")
plt.legend()
plt.grid(True)
plt.savefig("θ-ud1.png")  # 可以保存为其他格式，如PDF


# 递归计算防御方（端口关闭情况下）收益,n为递归轮次，pe为推断，r为当前轮次,θ为变量
def UD2payoff(xt, n, pe, round):
    # 博弈初始配置
    # 端口开放
    vh = 4
    # 端口关闭
    vl = 2
    # 测绘成本
    c = 1
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
        UD2 = pe * 1 * (-(t**n) * vl + (n + 1) * c) + (1 - pe) * (
            -(t ** (n - 1)) * vl + n * c
        )
        return UD2
    elif round == 0:
        UD2 = pe * 1 * (UD2payoff(xt, n, pe * (1 - xt), round + 1)) + (1 - pe) * (-vl)
        return UD2
    else:
        UD2 = pe * 1 * (UD2payoff(xt, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            -(t ** (round - 1)) * vl + round * c
        )
        return UD2


# 生成x轴数据
xt = np.linspace(0, 1, 100)
# 计算函数值
y2 = UD2payoff(xt, 5, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, y2, label="1experiment")
plt.title("Function Plot")
plt.xlabel("θ")
plt.ylabel("Ud2")
plt.legend()
plt.grid(True)
plt.savefig("θ-ud2.png")  # 可以保存为其他格式，如PDF


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
    x = 4
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


# 生成x轴数据
xt = np.linspace(0, 1, 100)
# 计算函数值
y = ADpayoff(xt, 6, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, y, label="1experiment")
plt.title("Function Plot")
plt.xlabel("θ")
plt.ylabel("Ua")
plt.legend()
plt.grid(True)
plt.savefig("θ-ua.png")  # 可以保存为其他格式，如PDF


# 递归计算攻击方（端口关闭情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def ADpayoff_left(t, n, pe, round):
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
    # 自然选择概率
    p = 0.5
    # 西塔
    xt = 0.23
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
                + (1 - xt) * (ADpayoff_left(t, n, pe * (1 - xt), round + 1))
            )
            + (1 - pe) * vh
        )
        return AD_l
    else:
        AD_l = pe * (
            xt * ((t**round) * vh - (round + 1) * c)
            + (1 - xt) * (ADpayoff_left(t, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (-(t ** (round - 1)) * vh - round * c)
        return AD_l


"""
# 递归计算攻击方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次,t为耐心
def ADpayoff_right(t, n, pe, round):
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
        AD_r = pe * 1 * (ADpayoff_right(t, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            vl - round * c
        )
        return AD_r
    else:
        AD_r = pe * 1 * (ADpayoff_right(t, n, pe * (1 - xt), round + 1)) + (1 - pe) * (
            (t ** (round - 1)) * vl - round * c
        )
        return AD_r


def ADpayoff(t, n, pe, round):
    return ADpayoff_right(t, n, pe, round) + ADpayoff_left(t, n, pe, round)


# 生成x轴数据
t = np.linspace(0, 1, 100)
# 计算函数值
y = ADpayoff(t, 10, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, y, label="1experiment")
plt.title("Function Plot")
plt.xlabel("t")
plt.ylabel("Ua")
plt.legend()
plt.grid(True)
plt.show()
plt.savefig("t-ua.png")  # 可以保存为其他格式，如PDF
"""
