def f(x, y, h):
    if x + y <= 20 and h == 3: return True
    elif x + y <= 20 and h < 3: return False
    elif x + y > 20 and h == 3: return False
    else:
        if h % 2 == 0:
            return any([f(x - 1, y, h + 1), f(x // 2, y, h + 1), f(x, y - 1, h + 1), f(x, y // 2, h + 1)])
        else:
            return any([f(x - 1, y, h + 1), f(x // 2, y, h + 1), f(x, y - 1, h + 1), f(x, y // 2, h + 1)])

for x in range(10, 100):
    if f(x, 10, 1):
        print(x)

# 43