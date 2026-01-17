p = float(input())

k = 1
t = 1

while 1 - t < p:
    t = t * (365 - k + 1) / 365
    k += 1

if k > 1:
    k -= 1

print(k)