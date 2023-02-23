def f(x, y, h):
    if h == 4 and x + y >= 61:
        return 1
    elif h == 4 and x + y < 61:
        return 0
    elif h < 4 and x + y >= 61:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, y, h + 1) or f(x * 4, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 4, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 4, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 4, h + 1)


for x in range(1, 57):
    if f(x, 3, 1) == 1:
        print(x)

# 12 14