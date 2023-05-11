for x in "0123456789AB":
    for y in "0123456789AB":
        num = int(x + "231" + y, 12) + int("78" + x + "98" + y, 14)
        if num % 99 == 0:
            print(num // 99)
