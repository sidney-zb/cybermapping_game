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


def f(xt):
    return UD1payoff(xt, 4, 0.5, 0)


"""
def find_minimum_recursive(x, step_size, precision):
    # 计算函数值
    fx = f(x)

    # 终止条件：如果函数值小于预定精度，返回当前 x 作为极小值
    if abs(fx) < precision:
        return x

    # 更新 x：在当前 x 处向函数下降最快的方向移动
    x -= step_size

    # 递归调用函数
    return find_minimum_recursive(x, step_size, precision)
"""

# 初始值、步长和精度
initial_x = 0.3
step_size = 1e-8
precision = 1e-4
x = initial_x
for i in range(0, 10000000):
    fx = f(x)

    # 终止条件：如果函数值小于预定精度，返回当前 x 作为极小值
    if abs(fx) < precision:
        break

    # 更新 x：在当前 x 处向函数下降最快的方向移动
    x -= step_size


print("极小值点:", x)
print("函数值:", f(x))
