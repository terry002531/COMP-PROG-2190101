def trans(s):
    result = ''
    n = len(s)
    for i in range(n):
        if 'A' <= s[i] <= 'Z':  # 大写字母
            result += chr((ord(s[i]) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= s[i] <= 'z':  # 小写字母
            result += chr((ord(s[i]) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += s[i]  # 其他字符原样保留
    return result

while True:
    a = str(input())
    if a == 'end':
        break
    print(trans(a))



# 方法二：直接‘两两对应’——比如 A↔N、B↔O、C↔P 这样去映射

# import string
#
# # 创建映射表
# rot13_table = str.maketrans(
#     string.ascii_uppercase + string.ascii_lowercase,
#     string.ascii_uppercase[13:] + string.ascii_uppercase[:13] +
#     string.ascii_lowercase[13:] + string.ascii_lowercase[:13]
# )
#
# # 主程序
# while True:
#     s = input()
#     if s == "end":
#         break
#     print(s.translate(rot13_table))
