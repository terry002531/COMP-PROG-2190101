# Exam1_A3-2: Mobile package billing

x = input().split()
A, B, C = int(x[0]), float(x[1]), int(x[2])   # A: plan(days), B: data(GB), C: calls(sec)

if A not in (10, 15, 30):
    print("InvalidPlan")
else:
    # base parameters
    if A == 10:
        base, free_data, free_call_min = 499, 40, 250
        data_rate, call_cost = 50, ("per_sec", 0.5)      # 0.5 per second
    elif A == 15:
        base, free_data, free_call_min = 699, 60, 300
        data_rate, call_cost = 75, ("per_min", 1)        # 1 per minute
    else:  # A == 30
        base, free_data, free_call_min = 1199, 100, 350
        data_rate, call_cost = 100, ("per_min", 1.5)     # 1.5 per minute

    total = base

    # extra data
    if B > free_data:
        total += (B - free_data) * data_rate

    # extra calls
    free_call_sec = free_call_min * 60
    if C > free_call_sec:
        extra_sec = C - free_call_sec
        if call_cost[0] == "per_sec":
            total += extra_sec * call_cost[1]
        else:  # per_min
            total += (extra_sec / 60) * call_cost[1]

    print(round(total))
