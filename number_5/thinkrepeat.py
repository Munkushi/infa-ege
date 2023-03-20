for i in range(202, 1000):
    n = bin(i)[2:]
    if n.count("0") == n.count("1"):
        n = n + n[-2]
    else:
        n = n + "1" if n.count("1") > n.count("0") else n +"0"
    if n.count("0") == n.count("1"):
        n = n + n[-2]
    else:
        n = n + "1" if n.count("1") > n.count("0") else n +"0" 
    if n.count("0") == n.count("1"):
        n = n + n[-2]
    else:
        n = n + "1" if n.count("1") > n.count("0") else n + "0"
    if n.count("0") == n.count("1"):
        n = n + n[-2]
    else:
        n = n + "1" if n.count("1") > n.count("0") else n + "0"
    r = int(n, 2)
    if r % 5 == 0:
        print(i)
        break

# 205 