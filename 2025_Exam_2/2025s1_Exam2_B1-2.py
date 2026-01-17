a = list(map(str,input().split()))
a.sort()
w = []
n = len(a)

w1 = []
for i in range(n):
    if a[i] != a[i-1] and abs(ord(a[i]) - ord(a[i-1])) != 1:
        w.append(w1)
        w1.sort(reverse=True)
        w1 = []
    w1.append(a[i])
    if i == n-1:
        w.append(w1)
        w1 = []

print(w[1:])