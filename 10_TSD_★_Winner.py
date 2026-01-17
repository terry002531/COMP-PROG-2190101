n = int(input())

win = []
lose = []

for i in range(n):
    a,b = input().split()
    win.append(str(a))
    lose.append(str(b))

winner = [x for x in win if x not in lose]

winner = list(set(winner))
print(sorted(winner))