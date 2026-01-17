s = input().strip().lower()  # 转小写，去除首尾空格
num = {}

# 统计每个英文字母的出现次数
for ch in s:
    if ch.isalpha():  # 只统计 a-z
        num[ch] = num.get(ch, 0) + 1

# 按规则排序：
#   - 先按出现次数降序（即负数），
#   - 再按字母升序
sorted_items = sorted(num.items(), key=lambda x: (-x[1], x[0]))

# 输出结果
for k, v in sorted_items:
    print(k,"->", v)
