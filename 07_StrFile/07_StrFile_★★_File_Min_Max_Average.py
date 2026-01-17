# 读取输入
name, year = input().split()
year2 = str(100 + int(year) % 100)  # 取年份后两位，比如 2562 -> "62"
year2 = year2[1:3]                 # 2005的后两位会变成“5”，补齐

# 打开文件
f = open(name, "r")

scores = []
n = 0
for line in f:
    line = line.strip()
    id, score = line.split()

    if id[:2] == year2:
        scores.append(float(score))
        n += 1

f.close()

if n == 0:
    print("No data")
else:
    print(round(min(scores),1),end=' ')
    print(round(max(scores),1),end=' ')
    print(round(sum(scores)/len(scores),1))




# scores = []
# for line in f:
#     parts = line.split()
#     if len(parts) != 2:
#         continue  # 跳过空行
#     sid = parts[0]
#     score = float(parts[1])
#
#     # 如果学号以 year2 开头（比如 "62"）
#     if sid[:2] == year2:
#         scores.append(score)
#
# f.close()
#
# # 输出结果
# if len(scores) == 0:
#     print("No data")
# else:
#     mn = min(scores)
#     mx = max(scores)
#     avg = sum(scores) / len(scores)
#     print(mn, mx, avg)
