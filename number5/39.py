for n in range(128, 256):
    n_8 = bin(n)[2:]
    n_8 = str(n_8)
    n_8 = n_8.replace("1", "*")
    n_8 = n_8.replace("0", "1")
    n_8 = n_8.replace("*", "0")
    r = int(n_8, 2)
    if n - r == 185:    print(n)

    # ?????/