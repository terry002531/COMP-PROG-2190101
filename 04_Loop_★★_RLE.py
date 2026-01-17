s = input()

count = 1
result = []

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        print(s[i - 1],count,'',end="")
        # result.append(f"{s[i - 1]} {count}")
        count = 1

# 处理最后一段

print(s[-1],count,end="")
# result.append(f"{s[-1]} {count}")
#
# print(" ".join(result))