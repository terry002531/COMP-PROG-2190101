n1 = int(input())
name1 = []
name2 = []
for i in range(n1):
    a, b = map(str,input().split())
    name1.append(a)
    name2.append(b)

n2 = int(input())
name = []
for i in range(n2):
    c = str(input())
    name.append(c)

n = 0

for i in range(0,n2):
    for j in range(0,n1):
        if name1[j] == name[i]:
            print(name2[j])
            n += 1
            break

for i in range(0,n2):
    for j in range(0,n1):
        if name2[j] == name[i]:
            print(name1[j])
            n += 1
            break

if n == 0:
    print("Not found")



# # First Name - Nickname
#
# n = int(input().strip())
# mp = {}
#
# for _ in range(n):
#     first, nick = input().split()
#     mp[first] = nick     # 正向：真名 -> 昵称
#     mp[nick]  = first    # 反向：昵称 -> 真名
#
# m = int(input().strip())
# for _ in range(m):
#     q = input().strip()
#     print(mp.get(q, "Not found"))
#                           # 从映射表 mp 中找 q 对应的名字或昵称；如果没有，输出 ‘Not found’
