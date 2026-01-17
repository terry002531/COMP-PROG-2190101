num = int(input())

x, y = [], []
for _ in range(num):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

s = input().strip()

mins = 1000000
maxs = -1000000

if s == "Zag-Zig":
    for i in range(num):
        if i % 2 == 0:
            mins = min(mins, y[i])
        else:
            mins = min(mins, x[i])
    for i in range(num):
        if i % 2 == 0:
            maxs = max(maxs, x[i])
        else:
            maxs = max(maxs, y[i])

elif s == "Zig-Zag":
    for i in range(num):
        if i % 2 == 0:
            mins = min(mins, x[i])
        else:
            mins = min(mins, y[i])
    for i in range(num):
        if i % 2 == 0:
            maxs = max(maxs, y[i])
        else:
            maxs = max(maxs, x[i])

print(mins, maxs)
