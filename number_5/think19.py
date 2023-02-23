for i in range(8000000, 100000000):
    a = str(i)
    sum1 = 0
    sum2 = 0

    for o in a:
        if int(o) % 2 == 0: 
            sum1 += int(o)

    for emochka in range(0, len(a), 2):
        sum2 += int(a[emochka])

    d = abs(sum1 - sum2)

    if d == 36:
        print(i)
        break

# answer = 9090909