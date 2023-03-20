def f(n):
    if n <= 0:
        return 1
    elif n > 0:
        return f(n-2) + f(n - 3) + 2 * n - 1


print(f(7))

# 51