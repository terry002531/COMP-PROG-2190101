def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append(float(e))
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= c
    return A

def mult(A, B):
    m = len(A)
    n = len(A[0])
    p = len(B[0])
    c = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += A[i][k] * B[k][j]
            c[i][j] = round(c[i][j], 1)
    return c

exec(input().strip())