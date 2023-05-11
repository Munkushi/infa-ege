for i in range(1, 100):
    n = str(bin(i)[2:])
    if i % 3 == 0:
        n += n[-3:]
    else:
        n += str(bin((i % 3) * 3)[2:])
    if int(n, 2) > 76:
        print(i)
        break    

