# word = input().strip()
# a = input()
#
# count = a.count(word)
#
# print(count)


key = input().strip()
s = input()

n = len(key)
cnt = 0
i = 0

while i <= len(s) - n:
    if s[i:i+n] == key:
        # 判断前后是否是边界或非字母
        left_ok = (i == 0) or (not s[i-1].isalpha())
        right_ok = (i+n == len(s)) or (not s[i+n].isalpha())
        if left_ok and right_ok:
            cnt += 1
    i += 1

print(cnt)

