import numpy as np
import matplotlib.pyplot as plt

# 生成 x 值
x = np.linspace(0, 2 * np.pi, 15)

# 生成不同的 y 值，例如 sin(x) 和 cos(x)
y1 = np.sin(x)
y2 = np.cos(x)

# 创建图表
plt.figure(figsize=(8, 6))

# 绘制红色虚线，不带标记的折线
plt.plot(x, y1, label="sin(x)", color="red", linestyle="-")

# 绘制蓝色实线，带有圆圈标记的折线
plt.plot(x, y2, label="cos(x)", color="blue", marker="o", linestyle="-")


# 添加标题和图例
plt.title("Sine and Cosine Functions")
plt.legend()

# 显示图表
plt.show()
