a = {'aaa':[1,2,3],'bbb':2,'ccc':3}
b = a['aaa']
print(a)
print(b)
for i in a.items():
    print(*i)
    print(type(i))
for i in a.keys():
    print(i)
    print(type(i))
for i in a.values():
    print(*i)
    print(type(i))
