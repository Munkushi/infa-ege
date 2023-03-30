def f(x, y, h):
    if (h == 3 or h == 5) and x + y <= 20: return True
    elif h < 5 and x + y <= 20: return False
    elif h == 5 and x + y > 20: return False
    else:
        if h % 2 == 0:
            return any([f(x - 1, y, h + 1), f(x, y - 1, h + 1), f(x // 2, y, h + 1), f(x, y // 2, h + 1)])
        return all([f(x - 1, y, h + 1), f(x, y - 1, h + 1), f(x // 2, y, h + 1), f(x, y // 2, h + 1)])

def f1(x, y, h):
    if h == 3 and x + y <= 20: return True
    elif h < 3 and x + y <= 20: return False
    elif h == 3 and x + y > 20: return False
    else:
        if h % 2 == 0:
            return any([f1(x - 1, y, h + 1), f1(x, y - 1, h + 1), f1(x // 2, y, h + 1), f1(x, y // 2, h + 1)])
        return all([f1(x - 1, y, h + 1), f1(x, y - 1, h + 1), f1(x // 2, y, h + 1), f1(x, y // 2, h + 1)])


for x in range(10, 100):
    if f(x, 10, 1):
        print(x)

print()

for x in range(10, 100):
    if f1(x, 10, 1):
        print(x)