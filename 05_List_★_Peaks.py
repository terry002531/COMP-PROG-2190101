a = list(map(int, input().split()))
l = len(a)

c = 0

for i in range(1,l-1):
    if a[i] > a[i + 1] and a[i] > a[i - 1]:
        c += 1

print(c)