lev = {1:'F',2:'D',3:'D+',4:'C',5:'C+',6:'B',7:'B+',8:'A'}
a = {}

def add(q):
    for k,v in lev.items():
        if v == a[q]:
            if k == 8:
                break
            a[q] = lev[k+1]
            break

while True:
    a3 = input().strip()
    if a3 == 'q':
        break
    a1,a2 = a3.split()
    a1 = a1.strip()
    a2 = a2.strip()
    a[a1] = a2

b = list(map(str, input().split()))
for i in b:
    add(i)

a = dict(sorted(a.items()))
for k, v in a.items():
    print(k, v)