import numpy as np
from scipy.optimize import minimize


# 步骤 2: 定义目标函数
def objective_function(x):
    return x**2 + 4 * x + 4  # 示例函数 f(x) = x^2 + 4x + 4


# 步骤 3: 使用优化算法（这里使用Nelder-Mead算法）
initial_guess = 0.0  # 步骤 4: 设置初始点
result = minimize(objective_function, initial_guess, method="Nelder-Mead")

# 步骤 6: 获取结果
minimum_x = result.x[0]  # 极值点的位置
minimum_value = result.fun  # 极小值

print(f"极小值点的位置: x = {minimum_x}")
print(f"极小值: f(x) = {minimum_value}")
