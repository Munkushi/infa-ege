def f(x, y, h):
    if x + y >= 75 and h == 4: return True
    elif x + y < 75 and h == 4: return False
    elif x + y >= 75 and h < 4: return False
    else:
        if h % 2 != 0:
            return any([f(x + 1, y, h + 1), f(x, y + 1, h + 1), f(x + y, y, h + 1), f(x, y + x, h + 1)])
        else:
            return all([f(x + 1, y, h + 1), f(x, y + 1, h + 1), f(x + y, y, h + 1), f(x, y + x, h + 1)])

for x in range(1, 67):
    if f(x, 7, 1):
        print(x)

# 20 33