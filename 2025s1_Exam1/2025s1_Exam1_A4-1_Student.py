# Exam1_A4-1: Sum of First N Fibonacci Numbers

N = int(input().strip())

if N == 0:
    print(0)
else:
    f1, f2 = 0, 1
    total = 0
    for i in range(1, N + 1):
        if i == 1:
            total += f1
        elif i == 2:
            total += f2
        else:
            f1, f2 = f2, f1 + f2
            total += f2
    print(total)
