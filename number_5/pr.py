for i in range(1, 100):
    n = bin(i)[2:]
    n = int(n)
    n = "10" + str(n) + "1" if n % 2 == 0 else "1" + str(n) + "01"
    r = int(n, 2)
    if r > 420:
        print(i)
        break