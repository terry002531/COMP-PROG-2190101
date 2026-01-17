# a, b = input().split()
#
# # 转换为整数
# num1 = int(a, 2)
# num2 = int(b, 2)
#
# # 求和
# s = num1 + num2
#
# # 转换回二进制，去掉前缀 0b
# print(bin(s)[2:])

#++++++++++++++++++++++++++++++++++++++++#

def main():
    b1, b2 = input().split()
    n1, n2 = int(b1,2), int(b2,2)
    #print(n1,n2)
    n = n1 + n2
    #print(bin(n))
    b = bin(n)[2:]
    print(b)

main()
