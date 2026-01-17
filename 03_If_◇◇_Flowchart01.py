a,b,c,d = map(int, input().split())

if a > b:
    a,b = b,a
    if d>= a:
        if c > d:
            c = c - a
    else:
        c = c + a
    b = a + c + d
else:
    if c > a >= b:
        d += a
    if d > c:
        b += 2
    else:
        b = b * 2

print(a,b,c,d)
