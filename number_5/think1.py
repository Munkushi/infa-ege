for i in range(1, 100):
    a = bin(i)[2::]
    if a.count("1") % 2 == 0: # or a += str(a.count("1") % 2) + "0"
        a += "00"
    else:
        a += "10"
    r = int(a, 2)
    if r > 119:
        print(i)
        break

# answer = 30