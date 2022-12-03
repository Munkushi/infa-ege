for n in range(1, 100):
    b = bin(n)[2:]
    b = str(b)
    if b.count("1") > b.count("0"):
        b = b + "1"
    elif b.count("0") > b.count("1") or b.count("0") == b.count("1"):
        b = b + "0"

    r = int(b, 2)
    if r > 80:
        print(r)
        break