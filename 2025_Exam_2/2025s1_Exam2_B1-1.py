a = list(map(int,input().split()))
a.sort()
n = len(a)
w = []
w1 = []

for i in range(n):
    if i == 0:
        w1.append(a[i])
    elif a[i] != a[i-1] and abs(a[i] - a[i-1]) != 1:
        w.append(w1)
        w1 = []
        w1.append(a[i])
    elif i == n-1:
        w1.append(a[i])
        w.append(w1)
    else:
        w1.append(a[i])

print(w)
