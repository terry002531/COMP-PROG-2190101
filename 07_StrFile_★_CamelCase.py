# camelCase: keep numbers, drop non-alnum, first word lower, others Capitalized
import re

s = input().strip()

# 提取所有由字母或数字组成的片段（去掉空格和符号）
tokens = re.findall(r'[A-Za-z0-9]+', s)

out = []
first_word_seen = False  # 只把第一个“字母词”设为全小写；纯数字不算“首词”

for t in tokens:
    if t.isdigit():
        out.append(t)                      # 数字原样拼接
    else:
        if not first_word_seen:
            out.append(t.lower())          # 第一个字母词全小写
            first_word_seen = True
        else:
            out.append(t[0].upper() + t[1:].lower())  # 之后每个词首字母大写，其余小写

print(''.join(out))
