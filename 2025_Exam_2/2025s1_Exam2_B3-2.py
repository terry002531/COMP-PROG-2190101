s = input().strip()
w = []

with open(s,'r') as f:
    for line in f:
        if '"' not in line:
            continue
        else:
            a,b,c = line.split('"')
            b = b.lower()
            w.append(b)
f.close()
print(w)
