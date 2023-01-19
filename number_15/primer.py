def f(d, x):
    return (((((x & 27) != 0) or ((x & d) == 0)) <= ((x & 26) != 0)) or ((x & d) != 0) or ((x & 37) == 0))


for d in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if f(d, x) == False:
            flag = False
            break
    if flag == True:
        print(d)

# min d = 37