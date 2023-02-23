for i in range(1, 100):
    # i = 4
    a = bin(i)[2:]
    a = str(a)
    summ = 0 
    for _ in a:
        summ += int(_, 2)
    if summ % 2 == 0:
        a = "1" + a[2:] + "0"
    else:
        a = "11" + a[2:] + "1"
    r =  int(a, 2)
    if r == 50: # r > 49
        print(i)
        
# print(r)
