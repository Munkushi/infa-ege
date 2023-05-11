for i in range(1, 100):
    n = bin(i)[2:]
    if n.count("1") % 2 == 0:
        n = "1" + n + "00"
    if n.count("1") % 2 != 0:
        n = "11" + n 
    if int(n, 2) >= 412:
        print(i)

# 9