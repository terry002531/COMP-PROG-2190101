a = {}

while True:
    w = input()
    if w == 'q':
        break
    w1,w2 = w.split(',')
    w1 = str(w1).strip()
    w2 = str(w2).strip()
    if w2 in a:
        a[w2].append(w1)
    else:
        a[w2] = [w1]

for w in a.items():
    print(w[0],end = ': ')
    print(', '.join(w[1]))