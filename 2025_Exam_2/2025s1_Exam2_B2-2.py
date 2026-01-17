def create_pricelist(text):
    pricelist = []
    w = list(map(str,text.split(", ")))
    for i in w:
        name,price = i.split("=")
        name = name.strip()
        price = price.strip()
        price = float(price)
        w1 = [name,price]
        pricelist.append(w1)
    return pricelist


def price_of(pricelist, item_name):
    for i in pricelist:
        if i[0] == item_name:
            return i[1]


def total(pricelist, s):
    w = list(map(str,s.split(" ")))
    to = 0
    q = 0
    for i in w:
        name,num = i.split(":")
        name = name.strip()
        num = int(num)
        if num == 0:
            pass
        else:
            q += 1
            s1 = f"{name} {num} {num * price_of(pricelist, name)}"
            print(s1)
            to += num * price_of(pricelist, name)
    if q <= 3:
        print(f"total {to}")
    else:
        to = round(to * 0.9,1)
        print(f"total {to}")

n = int(input())
for i in range(n):
    exec(input().strip())