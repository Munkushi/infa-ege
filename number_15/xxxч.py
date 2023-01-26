def f(x, y, a):
    return (2*x + 6*y < 235) or (x < y) or (a < x)

for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(x, y, a) == False:
                flag = False

    if flag == True:
        print(a)

# max a
# 29