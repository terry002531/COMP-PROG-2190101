def airfare(t, w, c):
    # 无效票
    if t not in [1, 2, 3]:
        return "InvalidTicket 0"

    # 根据票类型设定参数
    if t == 1:
        tp, fb, ef = 2000, 20, 500
    elif t == 2:
        tp, fb, ef = 5000, 30, 300
    else:  # t == 3
        tp, fb, ef = 8000, 40, 100

    # 计算基础票价
    total = tp

    # 计算超重行李费用
    extra = max(0, w - fb)
    if extra > 0:
        units = extra // 5
        if extra % 5 != 0:
            units += 1
        total += units * ef

    # 检查折扣码
    if len(c) != 8:
        return f"InvalidPromocode {total}"
    elif c[-3:] in ("UOB", "SCB"):
        total = round(total * 0.9)
        return f"Discount {total}"
    else:
        return f"NoDiscount {total}"


# 主程序
if __name__ == "__main__":
    x = input().split()
    t, w, c = int(x[0]), int(x[1]), x[2]
    print(airfare(t, w, c))
