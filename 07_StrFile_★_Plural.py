a = str(input())

a1 = a[-1:]
a2 = a[-2:]

ar1 = a[:-1]
ar2 = a[:-2]

if a1 == 's' or a1 == 'x' or a2 == 'ch':
    print(a + 'es')
elif a1 == 'y' and a[-2] not in 'aeiou':
    print(ar1 + 'ies')
else:
    print(a + 's')


