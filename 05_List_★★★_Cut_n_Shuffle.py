def cut(w):
    mid = int(len(w)/2)
    q = w[mid:] + w[:mid]
    return q

def sh(w):
    mid = int(len(w)/2)
    q = []
    q1 = w[:mid]
    q2 = w[mid:]
    for i in range(mid):
        q.append(q1[i])
        q.append(q2[i])
    return q

a = list(map(str,input().strip().split()))
b = str(input().strip())
for i in b:
    if i == 'C':
        a = cut(a)
    elif i == 'S':
        a = sh(a)
    else:
        pass
print(*a)