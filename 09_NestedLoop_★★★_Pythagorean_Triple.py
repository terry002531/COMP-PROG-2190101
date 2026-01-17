def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, b, c):
    w1 = gcd(a,b)
    w2 = gcd(b,c)
    w3 = gcd(a,c)
    w4 = gcd(w1, w2)
    w5 = gcd(w2, w3)
    if w5 == 1:
        return True
    else:
        return False

def primitive_Pythagorean_triples(max_len):
    c = []
    for i in range(1,max_len):
        for j in range(i+1, max_len):
            for k in range(j+1, max_len):
                if is_coprime(i, j, k) and i * i + j * j == k * k:
                    c.append([i, j, k])
    c = sorted(c, key=lambda x: (x[2], -x[1], x[0]))
    return c


exec(input().strip())