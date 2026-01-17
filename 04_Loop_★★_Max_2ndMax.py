# exec(input().strip())
w = str(input())
print("spj")
n = int(input())
a = {}
for i in range(n):
    a[i] = int(input())

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a[0],a[1])