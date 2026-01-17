def read_date():
    mname = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    data1 = input()
    d1, m11, y1 = data1.split()
    m1 = int(mname.index(m11)) + 1
    day = [int(d1), m1, int(y1)]
    return day

def zodiac(d,m):
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

def days_in_feb(y):
    if (y % 4 == 0):
        if (y % 100 == 0 and y % 400 != 0):
            return 28
        else:
            return 29
    else:
        return 28

def days_in_month(m, y):
    m = int(m)
    y = int(y)
    if(m == 2):
        days_in_feb(y)
    elif(m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12):
        return 31
    else:
        return 30

def days_in_between(d1, m1, y1, d2, m2, y2):
    day = 0
    day1 = days_in_month(m1, y1) - d1 + 1
    day2 = d2
    day = day1 + day2

    

def main():
    d1, m1, y1 = read_date()
    d2, m2, y2 = read_date()
    print(zodiac(d1, m1), zodiac(d2, m2))
    print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip())