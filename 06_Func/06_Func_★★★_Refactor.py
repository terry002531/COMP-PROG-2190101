# ----- helpers -----
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def is_leap(y: int) -> bool:
    return (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0)

def days_in_feb(y):
    return 29 if is_leap(y) else 28

def days_in_month(m, y):
    if m == 2:
        return days_in_feb(y)
    return 31 if m in (1,3,5,7,8,10,12) else 30

# ----- required functions -----
def read_date():
    d, mon, y = input().split()
    return [int(d), MONTHS.index(mon) + 1, int(y)]

def zodiac(d, m):
    if (d >= 22 and m == 3) or (d <= 21 and m == 4):  return "Aries"
    elif (d >= 22 and m == 4) or (d <= 21 and m == 5): return "Taurus"
    elif (d >= 22 and m == 5) or (d <= 21 and m == 6): return "Gemini"
    elif (d >= 22 and m == 6) or (d <= 21 and m == 7): return "Cancer"
    elif (d >= 22 and m == 7) or (d <= 21 and m == 8): return "Leo"
    elif (d >= 22 and m == 8) or (d <= 21 and m == 9): return "Virgo"
    elif (d >= 22 and m == 9) or (d <= 21 and m == 10):return "Libra"
    elif (d >= 22 and m == 10) or (d <= 21 and m == 11):return "Scorpio"
    elif (d >= 22 and m == 11) or (d <= 20 and m == 12):return "Sagittarius"
    elif (d >= 21 and m == 12) or (d <= 20 and m == 1): return "Capricorn"
    elif (d >= 21 and m == 1)  or (d <= 20 and m == 2): return "Aquarius"
    else:                                                     return "Pisces"

def days_in_between(d1, m1, y1, d2, m2, y2):
    # 完全复刻原题的大思路：
    # 剩余的 y1 年天数 + 中间整年用 int((y2-y1-1)*365.25) + y2 年已经过去的天数(不含当日)
    days = 0

    # y1：从 (d1,m1) 到年底
    days += days_in_month(m1, y1) - d1 + 1
    for mm in range(m1 + 1, 13):
        days += days_in_month(mm, y1)

    # 中间整年（近似 365.25，并向下取整）
    if y2 - y1 - 1 > 0:
        days += int((y2 - y1 - 1) * 365.25)

    # y2：从年初到 (d2,m2) 的前一天
    for mm in range(1, m2):
        days += days_in_month(mm, y2)
    days += (d2 - 1)

    return days

def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

# 评测器需要
exec(input().strip())
