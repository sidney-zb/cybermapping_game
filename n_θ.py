import numpy as np
import matplotlib.pyplot as plt


# 定义函数 f，使用 np.log 计算对数
def f(xt, ypxl, pi):
    return (np.log(ypxl / pi) / np.log(1 - xt)) + 1


# 生成x轴数据
xt = np.linspace(0, 0.99, 20)
# 计算函数值，这里的 0.002 仅作示例，你可以使用不同的 ypxl 值
ypxl1 = 0.1
n1 = f(xt, ypxl1, 0.5)
ypxl2 = 0.05
n2 = f(xt, ypxl2, 0.5)
ypxl3 = 0.01
n3 = f(xt, ypxl3, 0.5)

# 创建图像
plt.figure(figsize=(8, 6))

plt.plot(xt, n1, label="ε=0.1", marker="^", color="red", markersize="5")
plt.plot(xt, n2, label="ε=0.05", marker="o", color="blue", markersize="5")
plt.plot(xt, n3, label="ε=0.01", marker="*", color="green", markersize="5")
plt.title("n vs.θ")
plt.xlabel("θ")
plt.ylabel("n")
plt.legend()
plt.grid(False)
plt.show()
