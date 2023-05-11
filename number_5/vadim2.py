for i in range(1, 100):
    n = bin(i)[2:]
    if i % 3 == 0:
        n += n[:2]
    else:
        n += bin(i % 3)[2:]
    if int(n, 2) < 105:
        print(i)
        