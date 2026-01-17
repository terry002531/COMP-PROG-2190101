def index(ch):
    if 'a' <= ch <= 'z':
        return ord(ch) - ord('a')
    elif '0' <= ch <= '9':
        return 26 + ord(ch) - ord('0')
    else:
        return -1   # 非字母数字

s = input().lower()
w = input().lower()

count = [0] * 36

for ch in s:
    i = index(ch)
    if i != -1:
        count[i] += 1

for ch in w:
    i = index(ch)
    if i != -1:
        count[i] -= 1

if all(c == 0 for c in count):
    print("YES")
else:
    print("NO")
