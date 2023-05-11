for i in range(1200361, 12993610):
    if str(i)[0] == "1" and str(i)[1] == "2" and str(i)[4] == "3" and str(i)[5] == "6" and str(i)[-1] == "1":
        n = i
        if n % 273 == 0:
            print(n, n // 273)
    # if n % 273 == 0:
    #     print(n, n // 273)