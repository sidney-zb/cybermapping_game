import numpy as np
from matplotlib import pylab as pl

# 博弈初始配置
# 端口开放
vh = 4
# 端口关闭
vl = 2
# 测绘成本
c = 1
# 攻击方耐心
t = 0.5
# 自然选择概率
p = 0.5
# 西塔
xt = 0.5
# 期望推断p～
pe = 0
ua1 = 0.0
ua2 = 0.0

pe = p * (1 - xt)
ua1 = p * (
    (xt * t(vh - 2 * c) + (1 - xt) * t * (-vh - 2 * c)) + (1 - pe) * (-vh - c)
) + (pe(t * (vl - 2 * c)) + (1 - pe) * (vl - c))

ua2 = (p * (xt(vh - c) + (1 - xt) * ua1) + (1 - p) * (-vh)) + (p * ua1 + (1 - p) * vl)

print(ua1)

print(ua2)
