class Complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __str__(self):
        a = self.a
        b = self.b
        if a == 0 and b == 0:
            return "0"
        if a == 0:
            if b == 1:
                w = "i"
                return w
            if b == -1:
                w = "-i"
                return w
            else:
                w = f"{b}i"
                return w
        if b == 0:
            w = f"{a}"
            return w
        else:
            if b < 0:
                si = '-'
            else:
                si = '+'
            b = abs(b)
            if b == 1:
                return f"{a}{si}i"
            return f"{a}{si}{b}i"

    def __add__(self,rhs):
        return Complex(self.a+rhs.a, self.b+rhs.b)

    def __mul__(self,rhs):
        w1 = self.a * rhs.a - self.b * rhs.b
        w2 = self.a * rhs.b + self.b * rhs.a
        return Complex(w1,w2)

    def __truediv__(self,rhs):
        w1 = self.a * rhs.a + self.b * rhs.b
        w2 = - self.a * rhs.b + self.b * rhs.a
        w1 = w1 / (rhs.a **2 + rhs.b ** 2)
        w2 = w2 / (rhs.a **2 + rhs.b ** 2)
        return Complex(w1,w2)


t,a,b,c,d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)