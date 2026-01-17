import numpy as np

def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n,4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight,data

def report_lower_than_mean(weight,data):
    score = data[:,1]*weight[0] + data[:,2]*weight[1] + data[:,3]*weight[2]
    ave = np.mean(score)
    w = []
    for i in range(len(data)):
        if score[i] < ave:
            w.append(data[i,0])
    if w == []:
        print("None")
    else:
        for i in range(len(w)):
            if i < len(w)-1:
                print(w[i],end="")
                print(",",end=" ")
            else:
                print(w[i])

exec(input().strip())


# import numpy as np
#
# def read_data():
#     w = [float(e) for e in input().split()]
#     weight = np.array(w)
#     n = int(input())
#     data = np.ndarray((n, 4), int)
#     for i in range(n):
#         data[i] = [int(e) for e in input().split()]
#     return weight, data
#
# def report_lower_than_mean(weight, data):
#     # data[:,1:] 取出 midterm / final / project 三列
#     # weight 形状是 (3,)；(n,3)*(3,) 会广播成 (n,3)
#     scores = np.sum(data[:, 1:] * weight, axis=1)
#     # 也可以写：scores = data[:,1:].dot(weight)
#
#     mean_score = np.mean(scores)
#
#     # 找出低于平均分的学生
#     mask = scores < mean_score
#     ids = data[mask, 0]   # 取出对应行的 ID 列
#
#     if ids.size == 0:
#         print("None")
#     else:
#         print(", ".join(str(sid) for sid in ids))
#
# exec(input().strip())
