import math

# 分子部分
numerator = (
    math.pi
    - math.factorial(10) / (8 ** 8)
    + (math.log(9.7)) ** (7 / math.sqrt(71)
    - math.sin(math.radians(40)))  # 角度转弧度
)

# 分母部分
denominator = (1.2) ** (2.3 ** (1/3))

# 计算结果
result = numerator / denominator

# 保留 6 位小数
print(round(result, 6))
