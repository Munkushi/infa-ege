def f(n):
    global summ 
    summ += n + 3
    if n > 1:
        summ += n + 4
        f(n - 1)
        f(n - 2)


for n in range(1000):
    summ = 0
    f(n)
    if 1500 < summ < 2000:
        print(n)
        break
# 10