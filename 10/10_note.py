student1_score=['A1','10','30','40']
student2_score=['A2','8','25','35']
student3_score=['A3','9','27','31']
scores=[tuple(student1_score),tuple(student2_score),tuple(student3_score)]
print(*scores)          # ('A1', '10', '30', '40') ('A2', '8', '25', '35') ('A3', '9', '27', '31')
print(scores)           # [('A1', '10', '30', '40'), ('A2', '8', '25', '35'), ('A3', '9', '27', '31')]


a = [0]*10              # 快速初始化字典 a，a[0] - a[9] = 0
print(a)


a.add(100)              # 字典 a 加入数字100
a.remove(100)           # 字典 a 移除数字100


a = set(a)              # 去重，数据结构转为set集合
a = list(set(a))        # 去重，保持list的数据结构
a = a.intersection(a,b) # set a，b同时拥有的元素
a= a.union(a,b)         # set a，b的并集，无重复

winner = [x for x in win if x not in lose]  # 在list w 但是不在list lose的所有元素组成的list

with open(names, 'r') as f2:                # 读取文档
    for line in f1:
        a, b = line.split(',')
        a = int(a)
        courses[a] = b.strip()
f1.close()
