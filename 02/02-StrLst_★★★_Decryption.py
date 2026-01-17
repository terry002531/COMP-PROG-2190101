a = str(input())
a4 = int(a[3:4])
a11 = int(a[10:11])
a18 = int(a[17:18])
a25 = int(a[24:25])
a32 = int(a[31:32])
a8 = int(a[7:8])
a13 = int(a[12:13])
a23 = int(a[22:23])
a28 = int(a[27:28])

aaa = a4 * 10000 + a11 * 1000 + a18 * 100 + a25 * 10 + a32
bbb = a8 * 10000 + a13 * 1000 + a18 * 100 + a23 * 10 + a28
ccc = aaa + bbb + 10000

ddd = int((ccc % 10000 - ccc % 10) / 10)
e = ddd + 1000
f = str(e)
g = f[1:5]

# print(ddd)

sum = int(ddd / 100) + int(ddd % 100 / 10) + int(ddd % 10)
sum1 = str(sum)
no = int(sum % 10)

# print(sum)

word = ["A","B","C","D","E","F","G","H","I","J","K","L","M"]
word1 = word[no]
result = f"{g}{word1}"
print(result)