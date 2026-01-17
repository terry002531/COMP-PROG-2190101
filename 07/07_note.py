if a1 == 'y' and a[-2] not in 'aeiou':  # 如果以y结尾而且前一个字母不是元音（即不是 a, e, i, o, u）
    print(ar1 + 'ies')

s = "hello123"
if s.isalnum():
    print("只包含字母或数字")
else:
    print("包含其他字符")


ch = 'A'

if ch.islower():
    print("小写字母")
elif ch.isupper():
    print("大写字母")
else:
    print("不是字母")


for ch in s:                # 遍历字符串s中所有字符
    pass
ord(ch)                     # 把字符ch转成它的ASCII码值


f = open(name, "r")         # 打开文件
for line in f:              # 文件f里面有两列，一列是id，一列是成绩
    line = line.strip()     # 读入每一行，空格间隔储存到 sid 和 score 里
    id, score = line.split()


s = s.upper()               # s 字符串全部转为大写