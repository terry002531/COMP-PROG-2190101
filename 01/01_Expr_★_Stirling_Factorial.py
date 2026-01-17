import math

# 输入整数 n
n = int(input())

# 公共部分
common = math.sqrt(2 * math.pi) * (n ** (n + 0.5)) * math.exp(-n)

# 下界
lower = common * math.exp(1 / (12 * n + 1))

# 上界
upper = common * math.exp(1 / (12 * n))

# 输出
print(lower)
print(upper)
