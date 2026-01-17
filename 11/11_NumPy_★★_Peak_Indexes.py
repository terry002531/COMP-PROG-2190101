import numpy as np

def peak_indexes(x):
    if len(x) < 3:  # 少于3个数不可能有峰
        return np.array([], int)
    peaks = (x[1:-1] > x[:-2]) & (x[1:-1] > x[2:])
    return np.where(peaks)[0] + 1   # 加1修正索引位置

    # x1 = x[1:,:]
    # x2 = x[2:,:]
    # q = x1 > x and x1 > x2
    # w = num[q]
    # return w

def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")

exec(input().strip())