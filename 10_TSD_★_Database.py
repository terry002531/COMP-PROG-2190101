num = str(input().strip())
names = str(input().strip())
data = str(input().strip())

courses = {}
teachers = {}

with open(num, 'r') as f1:
    for line in f1:
        a,b = line.split(',')
        a = int(a)
        courses[a] = b.strip()
f1.close()

with open(names, 'r') as f2:
    for line in f2:
        a,b = line.split(',')
        a = int(a)
        teachers[a] = b.strip()
f2.close()

with open(data, 'r') as f3:
    for line in f3:
        line = line.strip()
        a,b = line.split(',')
        a = int(a)
        b = int(b)
        if a in courses and b in teachers:
            print(f"{courses[a]}, {teachers[b]}")
        else:
            print("record error")