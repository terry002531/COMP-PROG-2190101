total = 0.0
count = 0

while True:
    a = input()
    if a == "q":
        break
    total += float(a)
    count += 1

if count > 0:
    average = round(total / count, 2)
    print(average)
else:
    print("No Data")

