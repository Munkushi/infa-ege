def f(x, y, h):
    if x + y >= 63 and x + y <= 74 and h == 3: return True
    elif x + y < 63 or x + y >= 74 and h == 3: return False

    return f(x + 2, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 2, h + 1) or f(x, y * 2, h + 1)

for x in range(1, 241):
    if f(x, 17, 1):
        print(x)