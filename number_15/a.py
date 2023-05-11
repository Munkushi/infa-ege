def f(a, x, y):
    return (x >= 9) or ((2 * x) < y) or ((x * y) < a)



for a in range(101, 200):
    flag = True
    for x in range(0, 100):
        for y in range(0, 100):
            if f(a, x, y) == False:
                flag = False
                break
    if flag:
        print(a)
        break