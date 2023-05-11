def f(x, y, h):
    if h == 4 and x + y >= 93: return True
    elif h == 4 and x + y < 93: return False
    elif h < 4 and x + y >= 93: return False
    else:
        if h % 2 != 0:
            return any([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
        return all([f(x + 1, y, h + 1), f(x * 2, y, h + 1), f(x, y + 1, h + 1), f(x, y * 2, h + 1)])
for x in range(1, 80):
    if f(x, 12, 1):
        print(x)
        