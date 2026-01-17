#a = int(input())
#b = int(input())
#c = int(input())
#d = int(input())

st = str(input())

s = int(st)

d = int(s%10)
s/100
c = int(s%10)
s/100
b = int(s%10)
s/100
a = int(s%10)

x = 0
x-= 1 * b / (3 * a)
x-=1 / (3 * a) * (0.5 * (2 * b **3 - 9 * a * b * c + 27 * a*a*d + ((2*b**3 - 9*a*b*c + 27*a*a*d)**2 - 4*(b**2 - 3*a*c)**3) ** 0.5)) ** (1 / 3)
x-=1 / (3 * a) * (0.5 * (2 * b **3 - 9 * a * b * c + 27 * a*a*d - ((2*b**3 - 9*a*b*c + 27*a*a*d)**2 - 4*(b**2 - 3*a*c)**3) ** 0.5)) ** (1 / 3)

print(round(x , 3))