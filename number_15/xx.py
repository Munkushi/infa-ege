def f(a, x, y):
    return (112 != y + (x ** 2)) or (a < x) or (a < y)

for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if f(a, x, y) == False:
                flag = False
    if flag == True:
        print(a)

# max a 
# answer 11
