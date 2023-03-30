def f(n):
    if n <= 15:
        return n + 44
    elif n > 15 and n % 2 == 0:
        return f(n // 2) + n ** 4 - 18
    elif n > 15 and n % 2 != 0:
        return f(n - 2) + 3 * n ** 2 + 1
    
for x in range(1, 1001):
    # print(f(x))
    z = str(f(x))
    if z.count("1") == 5:
        print(z)