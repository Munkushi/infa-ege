for x in "0123456789ABCDE":
    num = int(f"97968{x}15", 15) + int(f"7{x}233", 15)
    if num % 14 == 0:
        print(num // 14)