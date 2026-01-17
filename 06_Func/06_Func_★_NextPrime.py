def is_prime(n):
    # Check if n is a prime number
    if n <= 1:
        return False
    # 只需试除到 sqrt(n)
    i = 2
    # 用 i*i <= n 避免每次开方
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def next_prime(N):
    # Return the least prime number which is more than N
    p = N + 1
    # 连续递增直到遇到质数
    while not is_prime(p):
        p += 1
    return p


def next_twin_prime(N):
    # Return the least twin prime number (p, p+2) with p > N
    # twin primes differ by 2, e.g., (11, 13)
    p = next_prime(N)          # 先找 >N 的下一个质数
    # 如果 p 和 p+2 不是孪生，就继续往后找
    while not is_prime(p + 2):
        p = next_prime(p)      # 跳到下一个质数再试
    return (p, p + 2)


# 必须保留这行以通过评测
exec(input().strip())
