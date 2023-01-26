def f(x, a):
    return (((x % 23 != 0) or ( x % 17 != 0)) <= ( x % a != 0))

for a in range(1, 480):
    flag = True
    for x in range(1, 1000):
        if f(x, a) == False:
            flag = False
    if flag == True:
        print(a)

# answer = 391