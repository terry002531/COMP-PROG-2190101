import numpy as np

x = 3.14159
print(np.floor(x * 1000) / 1000)    # 3.141  向下截断
print(np.ceil(x * 1000) / 1000)     # 3.142  向上截断
print()                             # 换行


import math
x = math.sqrt(10)
print(x)
print(round(x , 3))                 # 保四舍五入留小数点后三位
print(f"{x:.3g}")                   # 四舍五入保留三位sf


import math

print(math.radians(40))             # 角度转弧度
                                    # python标准库中所有三角函数默认使用弧度制

