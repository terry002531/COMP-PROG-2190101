a = list(map(float, input().split()))  # 输入4个实数，放入列表

highest = a[0]
lowest = a[0]       # 初始化最大最小

for x in a:         # 遍历找最大最小
    if x > highest:
        highest = x
    if x < lowest:
        lowest = x

total = 0
for x in a:
    total += x

final = (total - highest - lowest) / 2

print(round(final, 2))

