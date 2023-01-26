for i in range(100, 1000):
    fandt = int(str(i)[0]) * int(str(i)[1]) 
    sandt = int(str(i)[1]) * int(str(i)[2])
    if sandt > fandt:
        summ = str(fandt) + str(sandt)
    else:
        summ = str(sandt) + str(fandt)

    if summ == "621":
        print(i)
        break