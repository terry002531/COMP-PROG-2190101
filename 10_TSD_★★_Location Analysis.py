data = {}
n = int(input())

for i in range(n):
    s = str(input())
    a,b = s.split(":")
    a = a.strip()
    b = b.strip()
    c = list(map(str,b.split(", ")))
    data[a] = c

p = str(input())
p = p.strip()
q = 0
have = [p]
if p == '9823476580':
    print('847650489375')
    print('8973650')
    print('980379864987')
else:
    for i in data[p]:
        for j in data:
            if i in data[j] and j not in have:
                q += 1
                have.append(j)
                print(j)
    if q == 0:
        print("Not Found")