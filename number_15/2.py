def f(a, x):
    return (x&17 != 0) or (x&29 == 0) or (x&a != 0)

min_ = 64

for a in range(64):
    flag = True
    for x in range(64):
        if f(a, x) == False:
            flag = False
            break
    if flag == True:
        min_ = min(min_, a)

print(min_)