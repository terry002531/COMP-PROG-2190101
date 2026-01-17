a = str(input())
b = str(input())

la = len(a)
lb = len(b)
count = 0

if la == lb:
    for i in range(la):
        if a[i] == b[i]:
            count += 1
    print(count)
else:
    print("Incomplete answer")
