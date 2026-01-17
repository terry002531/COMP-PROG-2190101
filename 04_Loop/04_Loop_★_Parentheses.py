a = str(input())
a = list(a)

l = len(a)

for i in range(l):
    if(a[i] == "("):
        a[i] = "["
    elif (a[i] == "["):
        a[i] = "("
    elif (a[i] == ")"):
        a[i] = "]"
    elif (a[i] == "]"):
        a[i] = ")"

print("".join(a))   # 把列表拼接成字符串