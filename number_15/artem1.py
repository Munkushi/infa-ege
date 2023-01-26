def f(a, x):
    return ((a % 40) == 0) and (not ((780 % x) == 0) or(not((a % x) == 0) or not((180 % x) == 9)))

for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if f(a, x) == False:
            flag = False
            break
    if flag == False:
        print(a)

# ошибка где то
# решил на листике, см artem1NePy