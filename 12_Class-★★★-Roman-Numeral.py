class roman:
    def __init__(self, r):
        # 把罗马数字字符串 r 转成对应的整数，存在 self.value 里
        self.value = self._roman_to_int(r)

    # 用于 a < b 的比较
    def __lt__(self, rhs):
        return self.value < rhs.value

    # 用于 str(a)
    def __str__(self):
        return self._int_to_roman(self.value)

    # 用于 int(a)
    def __int__(self):
        return self.value

    # 用于 a + b，返回新的 roman 对象
    def __add__(self, rhs):
        total = self.value + rhs.value
        # 把和转换为标准罗马数字字符串，再创建新的 roman 对象
        return roman(self._int_to_roman(total))

    # ===== 内部工具函数：罗马数字 -> 整数 =====
    def _roman_to_int(s):
        vals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        while i < len(s):
            # 看看后一个是否比当前大（减法规则）
            if i + 1 < len(s) and vals[s[i]] < vals[s[i + 1]]:
                total += vals[s[i + 1]] - vals[s[i]]
                i += 2
            else:
                total += vals[s[i]]
                i += 1
        return total

    # ===== 内部工具函数：整数 -> 标准罗马数字字符串 =====
    def _int_to_roman(n):
        # 支持到 4999，4000–4999 用 MMMM... 形式（题目例子就是这样）
        pairs = [
            (1000, 'M'),
            (900,  'CM'),
            (500,  'D'),
            (400,  'CD'),
            (100,  'C'),
            (90,   'XC'),
            (50,   'L'),
            (40,   'XL'),
            (10,   'X'),
            (9,    'IX'),
            (5,    'V'),
            (4,    'IV'),
            (1,    'I')
        ]
        res = []
        for val, sym in pairs:
            while n >= val:
                res.append(sym)
                n -= val
        return ''.join(res)


# ===== 题目要求的主程序，直接放在类后面 =====
t, r1, r2 = input().split()
a = roman(r1)
b = roman(r2)

if t == '1':
    print(a < b)
elif t == '2':
    print(int(a), int(b))
elif t == '3':
    print(str(a), str(b))
elif t == '4':
    print(int(a + b))
else:
    print(str(a + b))
