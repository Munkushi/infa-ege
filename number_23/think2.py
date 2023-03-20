def f(x, y):
    if x > y or x == 16:
        return 0
    elif x == y:
        return 1
    return f(x + 2, y) + f(x + 4, y)

print(f(2, 36))

# 715