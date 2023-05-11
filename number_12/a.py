for i in range(4, 400):
    n = "3" + i * "5"
    while ("25" in n) or ("355" in n) or ("555" in n):
        if "25" in n:
            n = n.replace("25", "32", 1)
        if "355" in n:
            n = n.replace("355", "25", 1)
        if "555" in n:
            n = n.replace("555", "3", 1)
    m = 0
    n = n
    for j in n:
        m += int(j)
    if m == 17:
        print(i)