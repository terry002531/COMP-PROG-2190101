a[i].isdigit()              # 字符型 a[i] 是数字


from collections import deque

result = deque()            # 双端队列

result.append(10)           # 从右边加 → [10]
result.append(20)           # 从右边加 → [10, 20]
result.appendleft(5)        # 从左边加 → [5, 10, 20]


l = len(set(a))             # 列表 a 去重后的元素个数


m.sort()                    # 快排（从小到大）
m.sort(reverse=True)        # 快排（从大到小）


del n[0:15]                 # 删除0-15位
p = q.index(n)              # n 在列表 q 中的第几个

s = [10,20,30,40,50]
s[::2] = [10,30,50]         # 从头到尾，隔一个取一个（取偶数下标的元素）
s[:10:2] = [10,20,30]       # 从 索引 0 开始，到 索引 10 之前，每隔 2 个取一次
                            # s[start : stop : step]
