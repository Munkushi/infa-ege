for i in range(6, 50):
    n = "2" + i * "4"
    while ("14" in n) or ("244" in n) or ("444" in n):
        if ("14" in n):
            n = n.replace("14", "2", 1)
        if ("244" in n):
            n = n.replace("244", "14", 1)
        if ("444" in n):
            n = n.replace("444", "21", 1)
    summ = 0
    for z in n:
        summ += int(z)
    if summ > 20:
        print(i)