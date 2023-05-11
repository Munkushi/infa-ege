for x in "0123456789ABCDE":
    n = int("97968" + x + "13", 15) + int("7" + x + "213", 15)
    if n % 14 == 0:
        print(n // 14)