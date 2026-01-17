h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())

t1 = h1*3600 + m1*60 + s1
t2 = h2*3600 + m2*60 + s2

# 如果结束时间“看起来更早”，说明跨天了
if t2 < t1:
    t2 += 24*3600

dt = t2 - t1

dh = dt // 3600
dm = (dt % 3600) // 60
ds = dt % 60

print(f"{dh}:{dm}:{ds}")
