def f(x, a):
    return not ((x & 105) == 0) or ((not(x & 58) != 0) or (x & a) != 0)


for a in range(1, 100):
    flag = True
    for x in range(1, 1000):
        if f(x, a) == False:
            flag = False
            break
    if flag == True:
        print(a)

# min a 
# answer = 18