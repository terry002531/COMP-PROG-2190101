a = str(input().strip())
b = str(input().strip())
c = str(input().strip())

co = {}
re = {}

with open(a,'r') as f1:
    for line in f1:
        w1,w2 = line.split(',')
        co[w1] = w2.strip()
f1.close()
with open(b,'r') as f2:
    for line in f2:
        w1,w2 = line.split(',')
        re[w1] = w2.strip()
f2.close()

with open(c,'r') as f3:
    for line in f3:
        w1,w2 = line.split(',')
        w1 = w1.strip()
        w2 = w2.strip()
        if w1 in co and w2 in re:
            print(co[w1]+', '+re[w2])
        else:
            print('record error')