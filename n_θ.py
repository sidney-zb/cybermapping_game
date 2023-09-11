import numpy as np
import matplotlib.pyplot as plt


# 定义函数 f，使用 np.log 计算对数
def f(xt, ypxl, pi):
    return (np.log(ypxl / pi) / np.log(1 - xt)) + 1


# 生成x轴数据
xt = np.linspace(0, 0.99, 100)
# 计算函数值，这里的 0.002 仅作示例，你可以使用不同的 ypxl 值
ypxl = 0.01
n = f(xt, ypxl, 0.5)

# 创建图像
plt.figure(figsize=(8, 6))
plt.plot(xt, n, label="1experiment")
plt.title("Function Plot")
plt.xlabel("θ")
plt.ylabel("n")
plt.legend()
plt.grid(True)
plt.show()
