#u = eval(input())
#v = eval(input())

#result = [u[i] + v[i] for i in range(3)]

# 定义格式化函数：强制一位小数
def aaa(w):
    for i in range(3):
        if w[i]%1 == 0:
            w[i] = float(round(w[i],1))
    return "[" + ", ".join(f"{w[i]}" for i in range(3)) + "]"

# 输出
#print(f"{aaa(u)} + {aaa(v)} = {aaa(result)}")



u = ["u1", "u2", "u3"]
v = ["v1", "v2", "v3"]

u1,u2,u3 =map(float,input().strip("[]").split(","))
v1,v2,v3 = map(float,input().strip("[]").split(","))

x = u1 + v1
y = u2 + v2
z = u3 + v3


#print("[" , str(u1) , ", " , str(u2) , ", " , str(u3) , "] + [" , str(v1) , ", " + str(v2) , ", " + str(v3) , "] = [" , str(x) , ", " , str(y) , ", " , str(z) , "]")

print("[" + str(u1) + ", " + str(u2) + ", " + str(u3) + "] + [" \
      + str(v1) + ", " + str(v2) + ", " + str(v3) + "] = [" \
      + str(x) + ", " + str(y) + ", " + str(z) + "]")