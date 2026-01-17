a = str(input())
l = len(a)
s = {}

for i in range(10):
    s[i] = 0;

for i in range(l):
    if a[i].isdigit():
        s[int(a[i])] = 1;

j = 0

for i in range(10):
    if s[i] == 0:
        j += 1
        if j ==1:
            print(i, end="")
        else:
            print(",",end="")
            print(i, end="")

if j == 0:
    print("None")