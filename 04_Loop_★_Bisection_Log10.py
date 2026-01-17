a = float(input())

l = 0
u = a

while True:
    x = (l + u) / 2
    if abs(10**x - a) > 1e-10*x:
        if 10**x > a: u = x
        else:
            l = x
    else:
        break

print(round(x , 6))