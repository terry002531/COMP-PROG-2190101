n1 = int(input())
mp = {}
for i in range(n1):
    a,b = input().split()
    mp[a] = int(b)

n2 = int(input())
sale = {}

n = 0
for i in range(n2):
    c,d = input().split()
    d = int(d)
    if c in mp:
        if c in sale:
            sale[c] += mp[c] * d
        else:
            sale[c] = mp[c] * d
        n += 1

if n == 0:
    print("No ice cream sales ")

total = 0.0
if n != 0:
    for k, v in sale.items():
        total += v
    print("Total ice cream sales:", round(total, 1))

if n != 0:
    max_sale = max(sale.values())                     # 找出最高销售额
    top_names = []
    for k, v in sale.items():
        if v == max_sale:
            top_names.append(k)                       # 找出所有并列最高的名字
    top_names.sort()                                  # 按字母顺序排列
    print("Top sales:", ", ".join(top_names))         # 输出格式
