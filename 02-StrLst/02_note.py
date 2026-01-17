b = str(input())
a = len(b)
print(a)                # 取字符串长度


result = str(a).zfill(n)
                        # 把数字 a 先转成字符串，再在左边补零，直到字符串长度达到 n


i = a.find("/")         # 第一个 "/" 的位置


n0 = int(n[0:1])        # 截取字符串0-1（不包括1）


a, b, c, d = map(float, input().split())
                        # 以空格间隔输入


a = list(map(float, input().split()))
                        # 以空格间隔输入一个列表


import numpy as np
                        # 输入两个向量
u = np.array(eval(input()))   # 比如 [1, 2, 3]
v = np.array(eval(input()))   # 比如 [2, 3, 4]
                        # 向量相加
result = u + v


u = eval(input())       # 例如 [1, 2, 3]
v = eval(input())       # 例如 [2, 3, 4]
                        # 逐元素相加
result = [u[i] + v[i] for i in range(len(u))]


u1,u2,u3 =map(float,input().strip("[]").split(","))
                        # 把三维向量（格式如 [1.2, 3.4, 5.6]）解析成三个浮点数，分别存到 u1, u2, u3 里
                        # " .strip("[]") "  → 去掉前后的中括号
                        # " .split(",") "   → 按逗号分割