a.reshape(2,4)      # 矩阵a改为 2*4 形状
np.sum(A == 1)      # 计数 A 中等于 1 的元素数量
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
a[::2,:]            # 奇数行
a[1::2,:]           # 偶数行
a[:,::2]            # 奇数列
a[:,1::2]           # 偶数列
print(", ".join(str(sid) for sid in ids)) # 把数组 ids 中元素转为字符，用 , 连接


# 10-11
np.diag(A)          # 从左往右斜对角线元素
np.rot90(A)         # 逆时针旋转90度
A.T                 # 转置矩阵，行列互换
A.T[c][::-1]        # 取矩阵 A 的第 c 列，从下往上排列

# 10-12
w = wh[:,0]         # wh 中第一列的元素
h = wh[:,1]         # wh 中第二列的元素

# 10-13
np.exp(-l)          # e 的 -l 次方

# 10-21
upper = M[:mid, :]  # 上半部分,0-mid行
lower = M[mid:, :]  # 下半部分，mid-最后一行
M.shape             # (行数，列数)
M.shape[0]          # 行数
mid_row = M.shape[0] // 2
mid_col = M.shape[1] // 2

# 10-22
c = np.outer(a, b)  # cij = ai * bj； a是ix1的矩阵，b是jx1的矩阵，c是ixj

# 10-23

# 10-24
d = np.array([float(e) for e in input().split()]) # 从一行输入中读取若干数字（用空格分隔），并转换成 NumPy 浮点数组
np.where(peaks)[0]  # bool数组peaks中为true的位置，后面的[0]去除多于信息，只保留索引序号