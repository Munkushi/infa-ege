def f(x, y, h):
    if h == 4 and x + y >= 41:
        return 1
    elif h == 4 and x + y < 41:
        return 0
    elif h < 4 and x + y >= 41:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y + 2, h + 1) or f(x + 2, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y + 2, h + 1) and f(x + 2, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)

for x in range(1, 32):
    if f(x, 8, 1) == 1:
        print(x)

# max s = 14