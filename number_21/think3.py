def f(x, y, h):
    if x + y >= 75 and (h == 3 or h ==5): return True
    elif x + y >= 75 and h < 5: return False
    elif x + y < 75 and h == 5: return False
    else:
        if h % 2 == 0:
            return any([f(x + 1, y, h + 1), f(x, y + 1, h + 1), f(x + y, y, h + 1), f(x, y + x, h + 1)])
        else:
            return all([f(x + 1, y, h + 1), f(x, y + 1, h + 1), f(x + y, y, h + 1), f(x, y + x, h + 1)])

def f1(x, y, h):
    if x + y >= 75 and h == 3: return True
    elif x + y >= 75 and h < 3: return False
    elif x + y < 75 and h == 3: return False
    else:
        if h % 2 == 0:
            return any([f1(x + 1, y, h + 1), f1(x, y + 1, h + 1), f1(x + y, y, h + 1), f1(x, y + x, h + 1)])
        else:
            return all([f1(x + 1, y, h + 1), f1(x, y + 1, h + 1), f1(x + y, y, h + 1), f1(x, y + x, h + 1)])

for x in range(1, 67):
    if f(x, 7, 1):
        print(x)

print()

for x in range(1, 67):
    if f1(x, 7, 1):
        print(x)

# 32