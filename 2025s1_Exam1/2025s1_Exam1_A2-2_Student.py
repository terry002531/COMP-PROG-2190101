def phone_pet(phone: str) -> str:
    # 1. 检查格式
    if len(phone) != 13 or phone[0] != '(' or phone[4] != ')' or phone[8] != '-':
        return "Error1"

    # 2. 清理字符 (去掉 ( ) -)
    cleaned = phone.replace("(", "").replace(")", "").replace("-", "")

    # 3. 检查是否为10位数字
    if not cleaned.isdigit() or len(cleaned) != 10:
        return "Error2"

    # 4. 计算分数
    score = (int(cleaned[1]) * 2 + int(cleaned[3]) * 4 + int(cleaned[5]) * 6 +
             int(cleaned[7]) * 8 + int(cleaned[9]) * 10) % 100

    # 5. 对应宠物
    if 0 <= score <= 19:
        pet = "Cat"
    elif 20 <= score <= 39:
        pet = "Dog"
    elif 40 <= score <= 59:
        pet = "Bird"
    elif 60 <= score <= 79:
        pet = "Rabbit"
    else:
        pet = "Fish"

    return f"{cleaned}={pet}"


# 主程序
if __name__ == "__main__":
    phone = input().strip()
    print(phone_pet(phone))
