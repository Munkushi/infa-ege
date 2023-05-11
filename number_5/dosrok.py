for i in range(1, 100):
    n = bin(i)[2:]
    n = str(n)
    n = n + n[-3:] if i % 3 == 0 else n + str(bin(3 * (i % 3))[2:])
    # print(n)
    if int(n, 2) < 100:
        print(i)