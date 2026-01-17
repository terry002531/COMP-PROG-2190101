import math

# 输入
W = float(input())  # 体重 kg
H = float(input())  # 身高 cm

# Mosteller 公式
mosteller = math.sqrt(W * H) / 60

# Haycock 公式
haycock = 0.024265 * (W ** 0.5378) * (H ** 0.3964)

# Boyd 公式
boyd = 0.0333 * (W ** (0.6157 - 0.0188 * math.log10(W))) * (H ** 0.3)

# 输出
print(mosteller)
print(haycock)
print(boyd)
