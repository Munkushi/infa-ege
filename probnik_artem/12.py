for i in range(4, 50):
    n = "3" + i * "5"
    while ("25" in n) or ("355" in n) or ("555" in n):
        if ("25" in n):
            n = n.replace("25", "3", 1)
        if ("355" in n):
            n = n.replace("355", "52", 1)
        if ("555" in n):
            n = n.replace("555", "23", 1)
    summ = 0
    for z in n:
        summ += int(z)
    if summ == 27:
        print(i)