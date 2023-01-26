def f(x, y, a):
    return ((2*x + y) != 70) or (x < y) or (a < x)


for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(x, y, a) == False:
                flag = False
                break
    if flag == True:
        print(a)

# max a
# answer = 23
