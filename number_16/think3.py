def f(n):
    global summ
    if n > 0:
        summ += 3
        f(n - 2)
        f(n - 3)
        f(n - 2)
    summ += 3

summ = 0
f(17)
print(summ)

# 31011