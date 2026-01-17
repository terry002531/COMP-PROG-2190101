d = int(input())
m = int(input())
y = int(input())
y -= 543

day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
for i in range(m):
    d += day[i]

if y % 4 == 0 and y % 100 != 0 or y % 400 == 0 :
    d += 1
    # 能被 4 整除 的年份是闰年
    #
    # 但是能被 100 整除 的年份不是闰年
    #
    # 但是能被 400 整除 的年份仍然是闰年

print(d)