n = int(input())
list = {}
for i in range(n):
    a,b,value = input().split()
    key = f'{a} {b}'
    list[key] = value
    list[value] = key

n2 = int(input())
for i in range(n2):
    a = input()
    if a in list:
        print(a , "-->", list[a])
    else:
        print(a , "-->", "Not found ")