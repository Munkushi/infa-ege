def f(x, y, h):
    if h == 4 and x + y >= 231:
        return 1
    elif h == 4 and x + y < 231:
        return 0
    elif h < 4 and x + y >= 231:
        return 0
    else:
        if h % 2 != 0: # win
            return f(x + 1, y, h + 1) or f(x, y + 1, h + 1) or f(x * 2, y, h + 1) or f(x, y * 2, h + 1)
        else: # любой ход + луз
            return f(x + 1, y, h + 1) and f(x, y + 1, h + 1) and f(x * 2, y, h + 1) and f(x, y * 2, h + 1)


for x in range(1, 213):
    if f(x, 17, 1) == 1:
        print(x)

# 9 23 26