# 初始值、步长和精度
initial_x = 1.0
step_size = 0.01
precision = 1e-4
x = initial_x
for i in range(0, 100000000):
    fx = x**2 + 2 * x + 10
    # print(x)
    # 终止条件：如果函数值小于预定精度，返回当前 x 作为极小值
    if abs(fx) < precision:
        break
    # 更新 x：在当前 x 处向函数下降最快的方向移动
    x -= step_size


print("极小值:", x)
print("函数值:", x**2 + 2 * x + 10)
