def change(n):
    q = ['A', 'B+', 'B', 'C+', 'C', 'D+', 'D', 'F']
    p = q.index(n)
    if p == 0:                  # 如果已经是A了，就不变了
        return q[0]
    else:
        return q[p-1]


grades = {}
w = 0

while True:                     # 录入数据，直到遇到 q
    line = input().strip()
    if line == "q":
        break
    ids, grade = line.split()
    grades[w] = ids, grade
    w += 1

query = input().split()         # 最后一行：查询学号

for i in range(w):
    if grades[i][0] in query:   # 如果这个学生成绩需要修改
        print(grades[i][0],change(grades[i][1]))
    else:
        print(grades[i][0],grades[i][1])


# 直接 grades[学号] = 成绩

# grades = {}
#
# while True:                     # 录入数据，直到遇到 q
#     line = input().strip()
#     if line == "q":
#         break
#     ids, grade = line.split()
#     grades[ids] = grade         # 学号作为 key
#
# query = input().split()         # 最后一行：查询学号
#
# for sid, grade in grades.items():
#     if sid in query:            # 如果需要修改成绩
#         print(sid, change(grade))
#     else:
#         print(sid, grade)
