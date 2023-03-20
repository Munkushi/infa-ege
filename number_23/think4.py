def f(x, y):
    if x > y or x == 48:
        return 0
    elif x == y:
        return 1
    return f(x + 4, y) + f(x * 2, y) + f(x * 3, y)

print(f(16, 240))
# 261