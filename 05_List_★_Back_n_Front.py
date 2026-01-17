n = int(input())
a = []
b = []
c = []
q = []

for i in range(n):
    w = int(input())
    a.append(w)
b = list(map(int, input().split()))
while True:
    e = int(input())
    if e == -1:
        break
    else:
        c.append(e)

a = a[::-1]
b = b[::-1]
c = c[::-1]
q = c + b + a
q1 = q[::2]
q2 = q[1::2]
q2 = q2[::-1]
print(q1+q2)