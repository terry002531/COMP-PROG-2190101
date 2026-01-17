# Exam1_A4-2: Approximation of π

n = int(input().strip())

if n <= 0:
    print(0.0)
else:
    pi_approx = 0.0
    for k in range(n):
        pi_approx += ((-1)**k) / (2*k + 1)
    pi_approx *= 4
    print(round(pi_approx, 16))
