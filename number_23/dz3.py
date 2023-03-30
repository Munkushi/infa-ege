def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x + 1, y) + f(x + 2, y) + f(x + 9, y)
print(f(3, 7) * f(7, 16) * f(16, 27))