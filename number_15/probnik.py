def f(a, x, y):
    return (x > a) or (y > a) or ((2 * y + x) < 110)


for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(a, x, y) == False:
                flag = False
                break
    if flag == True:
        print(a)

# 36