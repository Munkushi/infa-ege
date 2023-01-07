count = 0
summ = 0

for i in range(1, 1000):
    s = i
    n = 1
    while s*s  > 10*n:
        s = s - 60
        n = n * 5
    
    if n == 625:
        count += 1
        summ += i
        print(count, summ)