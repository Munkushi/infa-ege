for i in range(4, 100):
    n = "3" + i * "5"
    while ("25" in n) or ("355" in n) or ("555" in n):
        if ("25" in n):
            n = n.replace("25", "3", 1)
        if ("355" in n):
            n = n.replace("355", "52", 1)
        if ("555" in n):
            n = n.replace("555", "23", 1)

    z = 0
    for m in n:
        z += int(m)
    if z == 27:
        print(i, n)