# d = list(map(int, input().split()))
#
# n = len(d)
# p = d[n - 1]
# i = -1
# j = 0
#
# if j >= n - 1:
#     d[i + 1], p = p, d[i + 1]
# else:
#     while j < n - 1:
#         if d[j] <= p:
#             i += 1
#             d[i], d[j] = d[j], d[i]
#         j += 1
#
# for i in range(n):
#     print(d[i], end=' ')

def partition_process():
    d = list(map(int, input().split()))
    n = len(d)
    p = d[-1]
    i = -1

    for j in range(n - 1):
        if d[j] <= p:
            i += 1
            d[i], d[j] = d[j], d[i]

    d[i + 1], d[-1] = d[-1], d[i + 1]

    print(d)

partition_process()



