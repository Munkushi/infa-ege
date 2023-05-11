def f(x, h):
    if (h == 3 or h == 5) and x >= 78: return True
    elif h == 5 and x < 78: return False
    elif h < 5 and x >= 78: return False
    else:
        if h % 2 == 0:
            return any([f(x + 1, h + 1), f(x + 4, h + 1), f(x * 4, h + 1)])
        else:
            return all([f(x + 1, h + 1), f(x + 4, h + 1), f(x * 4, h + 1)])

def f1(x, h):
    if h == 3 and x >= 78: return True
    elif h == 3 and x < 78: return False
    elif h < 3 and x >= 78: return False
    else:
        if h % 2 == 0:
            return any([f1(x + 1, h + 1), f1(x + 4, h + 1), f1(x * 4, h + 1)])
        else:
            return all([f1(x + 1, h + 1), f1(x + 4, h + 1), f1(x * 4, h + 1)])



for x in range(1, 77):
    if f(x, 1):
        print(x)

print()

for x in range(1, 77):
    if f1(x, 1):
        print(x)

# 14