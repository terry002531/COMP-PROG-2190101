import math

def v_1(a):
    r = a / 2
    v = math.pi * 4 / 3 * r**3
    return v

def v_2(a):
    v = a**3
    return v

a = float(input())
v = v_2(a) - v_1(a)
print(round(v , 2))