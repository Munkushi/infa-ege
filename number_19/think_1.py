def f(x, h):
    if h == 3 and x >= 63:
        return 1
    elif h == 3 and x < 63:
        return 0
    elif h < 3 and x >= 63:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x * 5, h + 1) or f(x + 4, h + 1)
        else:
            return f(x + 1, h + 1) or f(x * 5, h + 1) or f(x + 4, h + 1)

for x in range(1, 63):
    if f(x, 1) == 1:
        print(x)

# answer 3