def f(x, y, h):
    if (h == 3 or h == 5) and x + y >= 88:
        return 1
    elif h == 5 and x + y < 88:
        return 0
    elif h < 5 and x + y >= 88:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 3, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 3, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 3, h + 1)

def f1(x, y, h):
    if h == 3 and x + y >= 88:
        return 1
    elif h == 3 and x + y < 88:
        return 0
    elif h < 3 and x + y >= 88:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 3, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 3, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 3, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 3, h + 1)


for x in range(1, 72):
    if f(x, 6, 1) == 1:
        print(x)

print("---------------------")

for x in range(1, 72):
    if f(x, 6, 1) == 1:
        print(x)

# 27