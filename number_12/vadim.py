for i in range(4, 100):
    n = "3" +  i * "5"
    while ("25" in n) or ("355" in n) or ("555" in n):
        if ("25" in n):
            n = n.replace("25", "32", 1)
        if ("355" in n):
            n = n.replace("355", "25", 1)
        if ("555" in n):
            n = n.replace("555", "3", 1)
    if n.count("2") == 5:
        print(n, i)