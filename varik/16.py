def f(n):
    if n < 3:
        return 1024
    elif n > 2 and n % 2 == 0:
        return 6*f(n - 2) + 22
    elif  n > 2 and n % 2 != 0:
        return 36 * f(n - 4)


print(f(240) // f(180))