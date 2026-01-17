n = int(input())
lines = []
for i in range(n):
    s = str(input())
    lines.append(s)
    # lines[i] = str(input())

for i in range(n):
    con = 0
    for j in range(len(lines[i])):
        if lines[i][j] == '.':
            con += 1
        else:
            break
    con = int(con / 2)
    lines[i] = lines[i][con:]

# n = lines.index('#..1..')
# print(n)
# print(lines.index('#................5'))
for i in range(n):
    print(lines[i])
