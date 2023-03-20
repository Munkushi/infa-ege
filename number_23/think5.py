def f(n):
    global summ
    summ = n - 3
    if n > 3:
        summ = n + 15
        f(n - 2)
        f(n - 3)



for n in range(2000):
    summ = 0
    f(n)
    if summ > 2900000:
        print(n, summ)

# nice zadanie)