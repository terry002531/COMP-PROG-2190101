s = str("a b c")
s = list(s)         # 字符串s转为列表
s = "".join(s)      # 将列表s拼回字符串
print(s)


# .strip()      →   去掉首尾的空格/换行等
#
# .splitlines() →   按行分割字符串
#
# .split()      →   按空格分割字符串


i = 1
s[i].isalpha()      # 判断s[i]是不是字母或者汉字


print(" ", end='')  # 输出空格，不换行