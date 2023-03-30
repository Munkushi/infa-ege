def f(n):
    if n == 0:
        return 4
    elif 0 < n <= 12:
        return -f(n - 1)
    elif 13 < n < 77:
        return 4 * f(n - 3)
    elif n >= 77:
        return 14 * f(n - 3)
    
print(f(18))