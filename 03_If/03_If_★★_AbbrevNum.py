a = int(input())

def simplify(b):
    if b / 1000 > 10:
        b = int(round(b / 1000, 0))
    else:
        b = format(b / 1000, ".2g")
                # 保留2位significant figures
    return b

if a < 1000:
    print(a)
elif a < 1000000:
    a = simplify(a)
    print(str(a)+"K")
elif a < 1000000000:
    a = simplify(a / 1000)
    print(str(a)+"M")
else:
    a = simplify(a / 1000000)
    print(str(a)+"B")