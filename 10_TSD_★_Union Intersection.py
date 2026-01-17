n = int(input())

if n == 0:
    print(0)
    print(0)
else:

    w = list(map(int, input().split()))
    b = set(w)
    c = set(w)

    for i in range(n-1):
        a = list(map(int, input().split()))
        b = b.intersection(b, a)
        c = c.union(c,a)

    print(len(c))
    print(len(b))
