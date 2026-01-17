a = int(input())

n = []
n.append(a)


while a != 1:
    if a % 2 == 0:
        a = a / 2;
        n.append(a)
    else:
        a = a * 3 + 1
        n.append(a)

l = len(n)
if l > 15:
    del n[0:l-15]           # 删除前面的结果，只保留最后15步

print(int(n[0]), end = '')

for i in range(1,min(l,15)):
    print("->", end = '')
    print(int(n[i]), end = '')
