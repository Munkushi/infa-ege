b=0
i=0
for j in range (100, 3571):
    tmp = j
    a = 0
    while tmp % 7==0 and a < 3:
        a += 1
        tmp //= 7
    while tmp % 11==0 and a < 3:
        a += 1
        tmp //= 11
    while tmp % 17==0 and a < 3:
        a += 1
        tmp //= 17
    while tmp % 19==0 and a < 3:
        a += 1
        tmp //= 19
    if a==2:
        i += 1
        b += j 

s=int(b/i)
print(i,s)