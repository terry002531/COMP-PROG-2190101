pairs = [
    ("Robert", "Dick"),
    ("William", "Bill"),
    ("James", "Jim"),
    ("John", "Jack"),
    ("Margaret", "Peggy"),
    ("Edward", "Ed"),
    ("Sarah", "Sally"),
    ("Andrew", "Andy"),
    ("Anthony", "Tony"),
    ("Deborah", "Debbie")
]                       # 构建名字映射表

name = {}               # 双向字典

for full, nick in pairs:
    name[full] = nick
    name[nick] = full

n = int(input())        # 读取输入
for i in range(n):
    query = str(input())
    if query in name:
        print(name[query])
    else:
        print("Not found")
