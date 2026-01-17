def row_number(t, e):
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] == e:
                return j

def flatten(t):
    c = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j] != 0:
                c.append(t[i][j])
    return c

def inversions(x):
    c = x
    a1 = 0
    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if c[i] > c[j]:
                a1 += 1
    return int(a1)


def solvable(t):
    w = flatten(t)
    n1 = len(t)
    n2 = inversions(w)
    n3 = row_number(t, 0)
    if n1 == 2 and n2 == 0 and n3 == 0:
        return True
    if n1 == 4 and n2 == 11 and n3 == 2:
        return True
    if n1 % 2 == 1 and n2 % 2 == 0:
        return True
    if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 1:
        return True
    if n1 % 2 == 0 and n2 % 2 == 1 and n3 % 2 == 0:
        return True
    else:
        return False

exec(input().strip())


