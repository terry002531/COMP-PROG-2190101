a = float(input().strip())

L = 0
temp = a
U = 0
while temp >= 1:
    temp //= 10
    U += 1

while True:
    M = (L + U) / 2
    val = 10 ** M
    if abs(val - a) <= 1e-10 * max(val, a):
        break
    if val < a:
        L = M
    else:
        U = M

print(round(M , 6))
