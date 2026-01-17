def first_fit(L, e):
    for i in range(len(L)):
        if len(L[i]) == 1:
            L[i].append(e)
            break

def best_fit(L, e):
    diff = []
    for i in range(len(L)):
        s = sum(L[i])
        d = abs(s + e - 100)
        diff.append([d, i])
    diff.sort()
    ind = diff[0][1]
    L[ind].append(e)

def partition_FF(D):
    pass

exec(input().strip())
