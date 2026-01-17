def s(s1,s2):
    s1a,s1b = s1.split(':')
    s2a,s2b = s2.split(':')
    s1a,s1b = int(s1a),int(s1b)
    s2a,s2b = int(s2a),int(s2b)
    if s1b+s2b >= 60:
        s3b = s1b+s2b-60
        s3a = s1a+s2a+1
    else:
        s3b = s1b+s2b
        s3a = s1a+s2a
    s3a = str(s3a)
    s3b = str(s3b).zfill(2)
    x = f"{s3a}:{s3b}"
    return x

def ch(x):
    a,b = x.split(':')
    a,b = int(a),int(b)
    return a*60 + b

n = int(input())
w = {}
for i in range(n):
    q,w1,w2,w3 = map(str,input().strip().split(', '))
    if w2 in w:
        w[w2] = s(w[w2],w3)
    else:
        w[w2] = w3

so = sorted(w.items(),key=lambda x: ch(x[1]),reverse=True)

c = 0
for k,v in so:
    if c == 3:
        break
    print(k,'-->',v)
    c += 1