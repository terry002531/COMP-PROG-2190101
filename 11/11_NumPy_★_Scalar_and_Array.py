import numpy as np

def toCelsius(f):
    return (f - 32) * 5 / 9

def BMI(wh):
    w = wh[:,0]
    h = wh[:,1] / 100
    return w / h / h

def distanceTo(p, Points):
    dx = Points[:, 0] - p[0]  # 所有点的 x 与 p 的 x 差
    dy = Points[:, 1] - p[1]  # 所有点的 y 与 p 的 y 差
    return np.sqrt(dx ** 2 + dy ** 2)

exec(input().strip())

