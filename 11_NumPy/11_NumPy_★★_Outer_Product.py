import numpy as np

def mult_table(nrows, ncols):
    a = np.arange(1, nrows+1)
    b = np.arange(1, ncols+1)
    return np.outer(a, b)

exec(input().strip())