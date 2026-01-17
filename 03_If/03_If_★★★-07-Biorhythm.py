# d1,m1,y1,d2,m2,y2 = map(int, input().split())
#
# def day_count(d,m,y):
#     y -= 543
#     day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     for i in range(m):
#         d += day[i]
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         d -= 1
#     return d
#
# day1 = day_count(d1,m1,y1)
# day2 = day_count(d2,m2,y2)
#
# total = (y2 - y1) * 365 + day2 - day1
#
# print(total)

import math

# 读入：bd, bm, by(BE), d, m, y(BE)
bd, bm, by_be, d, m, y_be = map(int, input().split())

# BE -> AD
by = by_be - 543
y  = y_be  - 543

def is_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def days_in_month(year: int, month: int) -> int:
    if month == 2:
        return 29 if is_leap(year) else 28
    if month in (1,3,5,7,8,10,12):
        return 31
    return 30

# 红段：从“出生当日（含）”到当年12/31（含）
red = 0
# 出生当月（含出生当日）
red += days_in_month(by, bm) - bd + 1   # 关键修正：+1 把出生当日计入
# 之后到12月的整月
for mm in range(bm + 1, 13):
    red += days_in_month(by, mm)

# 黑段：中间完整年份 × 365（题面明确要求忽略闰日）
full_years_between = max(0, y - by - 1)
black = full_years_between * 365

# 蓝段：目标年1/1 到“目标日前一日”（不含目标日）
blue = 0
for mm in range(1, m):
    blue += days_in_month(y, mm)
blue += (d - 1)

# 总天数
x = red + black + blue

# 三个生物节律值
phys = math.sin(2 * math.pi * x / 23)   # physical
emot = math.sin(2 * math.pi * x / 28)   # emotional
intel = math.sin(2 * math.pi * x / 33)  # intellectual

# 输出
print(x, f"{phys:.2f}", f"{emot:.2f}", f"{intel:.2f}")
