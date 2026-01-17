def factor(N):
    fa = []
    for i in range(2,N + 2):
        con = 0
        while N % i == 0:
            if(N // i % i != 0):
                fa.append([i, con + 1])
            con += 1
            N = N // i
    return fa

exec(input().strip())