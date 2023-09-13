import numpy as np
from matplotlib import pylab as plt


def f(xt, n):
    return ((1 - xt) ** (n - 1)) * 0.5


# 生成x轴数据
xt = np.linspace(0, 1, 15)
# 计算函数值
y1 = f(xt, 5)
y2 = f(xt, 8)
y3 = f(xt, 10)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, y1, label="n=5,p=0.5", marker="^", color="red", markersize="5")
plt.plot(xt, y2, label="n=8,p=0.5", marker="o", color="blue", markersize="5")
plt.plot(xt, y3, label="n=10,p=0.5", marker="*", color="green", markersize="5")
plt.title("p~ vs. θ")
plt.xlabel("θ")
plt.ylabel("p~")
plt.legend()
plt.grid(False)
plt.show()
