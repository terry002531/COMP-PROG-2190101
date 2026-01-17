import numpy as np

def p(x):
    so = x[:,0]
    g = x[:,1]
    l = -3.98 + 0.1 * so + 0.5 * g
    q = 1 / (1 + np.exp(-l))
    return q

exec(input().strip())
