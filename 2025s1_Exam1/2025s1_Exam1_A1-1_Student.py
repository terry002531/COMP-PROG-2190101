import math

def volume( r ):
    n = 2 * r / 3**0.5
    v = (math.pi * 4 / 3 * r**3) - n**3
    return v

a = float(input())
v = volume( a )
print(round(v , 2))
