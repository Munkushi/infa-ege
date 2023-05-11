for i in range(1, 100):
    n = bin(i)[2:]
    n += n[:2][::-1]

    if int(n, 2) > 90:
        print(i)
        break