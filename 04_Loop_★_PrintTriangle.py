a = int(input())

for i in range(a - 1):
    print(" ", end='')
print("*")

for i in range(2,a):
    for j in range(a - i):
        print(" ", end='')
    print("*", end="")
    for j in range(2 * i - 3):
        print(" ", end='')
    print("*")

for i in range(2 * a - 1):
    print("*", end='')