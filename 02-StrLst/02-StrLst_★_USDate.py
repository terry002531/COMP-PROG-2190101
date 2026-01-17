a = input()
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# 找到第一个和第二个 "/"
i = a.find("/")        # 第一个 "/" 的位置
j = a.find("/", i+1)   # 第二个 "/" 的位置

day = int(a[0:i])
month = int(a[i+1:j])
year = int(a[j+1:])

result = f"{months[month - 1]} {int(day)}, {year}"

print(result)