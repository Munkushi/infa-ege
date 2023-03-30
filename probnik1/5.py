z = []
for i in range(1, 100):
    n = bin(i)[2:]
    n = str(n)
    if n.count("1") % 2 == 0:
        n = "101" + n[3:] + "00"
    elif n.count("1") % 2 != 0:
        n = "11" + n[2:] + "11"
    if int(n, 2) > 401:
        print(i)
        break
