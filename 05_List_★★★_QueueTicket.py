q = []                 # 等待队列
times = {}             # 记录取号时间
waits = []             # 记录所有等待时间
current = None         # 当前叫到的号码
ticket_num = None      # 当前票号（初始化后自增）

n = int(input())       # 命令数量

for _ in range(n):
    c = input().split()
    if c[0] == "reset":
        ticket_num = int(c[1])
        q = []
        times = {}
        waits = []
        current = None

    elif c[0] == "new":
        t = int(c[1])
        print("ticket", ticket_num)
        q.append(ticket_num)
        times[ticket_num] = t
        ticket_num += 1

    elif c[0] == "next":
        if q:
            current = q.pop(0)
            print("call", current)

    elif c[0] == "order":
        t = int(c[1])
        if current is not None:
            dt = t - times[current]
            waits.append(dt)
            print("qtime", current, dt)

    elif c[0] == "avg_qtime":
        if waits:
            avg = sum(waits) / len(waits)
            print("avg_qtime", round(avg, 4))
