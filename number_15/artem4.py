def f(a, x, y):
    return (3*x + 7*y < a) or (x >= y) or (y > 6)

for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(a, x, y) == False:
                flag = False
                break
    if flag == True:
        print(a)

# min a
# answer = 58
