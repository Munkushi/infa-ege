def f(a, x):
    return ((a % 45 == 0) and (not (750 % x == 0) or ((a % x == 0) or not (120 % x == 0))))

c = 0

for a in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if f(a, x) == False:
            flag = False
            break
    if flag:
        print(a)
        c += 1

print(c)