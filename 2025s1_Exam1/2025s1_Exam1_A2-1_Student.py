def phone_personality(phone: str) -> str:
    # 1. 检查格式
    if len(phone) != 12 or phone[3] != '-' or phone[7] != '-':
        return "Error1"

    # 2. 去掉 -
    cleaned = phone.replace("-", "")

    # 3. 检查是否为10位数字
    if not cleaned.isdigit() or len(cleaned) != 10:
        return "Error2"

    # 4. 计算 personality 分数
    score = (int(cleaned[0]) * 1 + int(cleaned[2]) * 3 + int(cleaned[4]) * 5 +
             int(cleaned[6]) * 7 + int(cleaned[8]) * 9) % 100

    # 5. personality 分类
    if 0 <= score <= 19:
        personality = "Calm"
    elif 20 <= score <= 39:
        personality = "Creative"
    elif 40 <= score <= 59:
        personality = "Energetic"
    elif 60 <= score <= 79:
        personality = "Practical"
    else:
        personality = "Lucky"

    return f"{cleaned}={personality}"


# 主程序
if __name__ == "__main__":
    phone = input().strip()
    print(phone_personality(phone))
