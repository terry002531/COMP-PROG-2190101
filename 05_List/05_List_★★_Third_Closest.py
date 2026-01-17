import math
n = int(input())
a = {}
distance = {}
for i in range(n):
    x,y = map(float, input().split())
    a[i] = (x,y)
    distance[i] = math.sqrt(x**2 + y**2)
distance = sorted(distance.items(), key=lambda item: item[1])
c = 1
for k, v in distance:
    if c == 3:
        print(f'#{k+1}: {a[k]}')
        break
    c += 1
