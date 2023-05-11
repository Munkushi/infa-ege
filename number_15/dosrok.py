def f(a, x):
    return (x & 39) == 0 or (not ((x & 11)  == 0) or not((x & a) == 0))


cnt = 0
for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if f(a, x) == False:
            flag = False
            break
    if flag == True:
        print(a)