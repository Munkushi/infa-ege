def f(x, a):
    return ((x & 135) != 0) <= (((x & 233) == 0) <= ((x & a) != 0))

for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if f(x, a) == False:
            flag = False
    
    if flag == True:
        print(a)

# min a
# answer 6