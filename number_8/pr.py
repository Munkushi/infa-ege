z = set()
for i in range(1, 1000):
    n = i*"1"

    while ("1111" in n) or ("222" in n) or ("33" in n):
        if ("1111" in n):
            n = n.replace("1111", "333", 1)
        elif ("222" in n):
            n = n.replace("222", "11", 1)
        elif ("33" in n):
            n = n.replace("33", "2", 1)
    z.add(n)
print(len(z))