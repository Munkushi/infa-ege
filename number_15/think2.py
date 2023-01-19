def f(x, y, a):
    return ((15 * x + 14 * y) != 240) or (a < (15 * x + 13 * y)) and (a > (2 * y + 11 * x - 342))


for a in range(100, 1000):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(a, x, y) == False:
                flag = False
                break

    if flag == True:
        print(a)

# неправильно