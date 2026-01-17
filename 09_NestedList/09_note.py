lines = ['a', 'b', 'c']
print(lines.index('c'))                 # 2


b = w.count(a)                              # 数字 a 在列表 w 中的个数

def factor(N):
    fa = []
    for i in range(2,N + 2):
        con = 0
        while N % i == 0:
            if(N // i % i != 0):
                fa.append([i, con + 1])
            con += 1
            N = N // i
    return fa
print(factor(200))                      # 嵌套列表的应用   [[2, 3], [5, 2]]


x = input().split()
while x[0] != 'q':
    a, b = int(x[0]), int(x[1])
    while b != 0:
        a, b = b, a % b
    print(a)
    x = input().split()                 # 计算最大公约数 GCD


students = [["Renee", 1989, ["Drama1", "Drama2"]],
            ["Alex", 1990, ["FilmA", "FilmB"]]]
a = students[0]                         # ["Renee", 1989, ["Drama1", "Drama2"]
b = students[0][0]                      # Renee
c = students[0][1]                      # 1989
d = students[0][2]                      # ["Drama1", "Drama2"]
e = students[0][2][0]                   # Drama1
f = students[0][2][1]                   # Drama2         # 嵌套列表


x = []
for i in range(5):
    x.append([0])                       # 嵌套列表初始化

c = [[0 for _ in range(p)] for _ in range(m)]
                                        # c 初始化为 m 行 p 列的全 0 矩阵


lst = [1, 2, 3, 4, 5, [6], 'a']
reversed_lst = lst[::-1]                # 列表翻转   ['a', [6], 5, 4, 3, 2, 1]


x = [1,2,3,4]
y = [v * 2 for v in x]                  # [2,4,6,8]
w = [v for v in x if v % 2 == 0]        # [2,4]
for i in range(len(x)):
    x[i] =  x[i] * 2                    # [2,4,6,8]
z = x * 2                               # [2, 4, 6, 8, 2, 4, 6, 8]


nums = [int(e) for e in input().split()]# 从输入行读取数据


words = ["your", "heart", "is", "on", "my", "list"]
pairs = [[len(w), w] for w in words]    # [[4, 'your'], [5, 'heart'], [2, 'is'], [2, 'on'], [2, 'my'], [4, 'list']]
pairs.sort()    # 根据字符串长度排序        # [[2, 'is'], [2, 'my'], [2, 'on'], [4, 'list'], [4, 'your'], [5, 'heart']]
p = [pairs[1] for pairs in pairs]       # ['is', 'my', 'on', 'list', 'your', 'heart']


i = len(A)                              # 矩阵 A 有多少行
j = len(A[0])                           # 矩阵 A 有多少列


def mult(A, B):                         # A m行n列， B n行p列
    m = len(A)                          # 矩阵 A 有多少行
    n = len(A[0])                       # 矩阵 A 有多少列
    p = len(B[0])
    c = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                c[i][j] += A[i][k] * B[k][j]
            c[i][j] = round(c[i][j], 1)
    return c                            # 矩阵计算
                                        # 答案 c m行p列
