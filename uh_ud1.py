import numpy as np
from matplotlib import pylab as plt


#  递归计算防御方（端口开放情况下）收益,n为递归轮次，pe为推断，r为当前轮次
def UD1payoff(vh, n, pe, round):
    # 博弈初始配置
    # 端口开放
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
    xt = 0.3
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
            + (1 - xt) * (UD1payoff(vh, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * (vh + round * c - round * x)
        return UD1
    else:
        UD1 = pe * (
            xt * (-(t**round) * vh + (round + 1) * c - (round * x))
            + (1 - xt) * (UD1payoff(vh, n, pe * (1 - xt), round + 1))
        ) + (1 - pe) * ((t ** (round - 1)) * vh + round * c - round * x)

        return UD1

    # 生成x轴数据


vh = np.linspace(1, 10, 100)
# 计算函数值
ud1 = UD1payoff(vh, 10, 0.5, 0)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(vh, ud1, label="1experiment")
plt.title("Function Plot")
plt.xlabel("uh")
plt.ylabel("Ud1")
plt.legend()
plt.grid(True)
plt.savefig("uh-ud1.png")  # 可以保存为其他格式，如PDF
