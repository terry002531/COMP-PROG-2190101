a = list(map(float, input().split()))

highest = max(a)   # 最高分
lowest = min(a)    # 最低分

total = sum(a)     # 总和
final = (total - highest - lowest) / 2

print(round(final, 2))
