for i in range(1 , 300):
    a = bin(i)[2:]
    a = (8 - len(a)) * "0" + a # чтобы добить длинну до 8 или можно через len
    a = a.replace("0", "*")
    a = a.replace("1", "0")
    a = a.replace("*", "1")
    r = int(a, 2)
    if r - i == 31:
        print(i)

# answer = 112