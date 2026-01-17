import sys

def r(s):
    n = len(s)
    s = s[::-1]
    for i in range(n):
        if s[i] == 'A': print('T',end = '')
        elif s[i] == 'C': print('G',end = '')
        elif s[i] == 'T': print('A',end = '')
        elif s[i] == 'G': print('C',end = '')

def f(s):
    n = len(s)
    a = t = g = c = 0
    for i in range(n):
        if s[i] == 'A':
            a += 1
        if s[i] == 'C':
            c += 1
        if s[i] == 'T':
            t += 1
        if s[i] == 'G':
            g += 1
    print("A" + "=" ,end = '')
    print(a , end = ', ')
    print("T" + "=", end='')
    print(t, end=', ')
    print("G" + "=" ,end = '')
    print(g , end = ', ')
    print("C" + "=", end='')
    print(c, end=' ')

def d(s,t):
    n = len(s)
    w = len(t)
    c = 0
    for i in range(n-w+1):
        if s[i:i+w] == t:
            c += 1
    print(c)

s = str(input())
order = str(input())
if order == 'D':
    o = str(input())
n = len(s)

s = s.upper()

for i in range(n):
    if s[i] != 'A' and s[i] != 'C' and s[i] != 'T' and s[i] != 'G':
        print("Invalid DNA")
        sys.exit()

if order == 'R':
    r(s)
if order == 'F':
    f(s)
if order == 'D':
    d(s,o)
