def f(a, x):
    return (x & 49 != 0) <= ((x & 33 == 0) <= ((x & a) != 0))

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(a, x) == False:
            flag = False
            break
    if flag == True:
        print(a)