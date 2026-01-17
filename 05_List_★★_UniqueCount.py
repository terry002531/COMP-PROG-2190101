a = list(map(int, input().split()))
l = len(a)

num = {}
c = 0
m = []

for i in range(l):
    if a[i] not in num:      # 第一次出现
        num[a[i]] = 1
        c += 1
        m.append(a[i])
    else:
        num[a[i]] += 1       # 已经有了就加 1

print(c)

m.sort()

print(m[:10])