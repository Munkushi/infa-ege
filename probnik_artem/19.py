def f(x, h):
    if x >= 78 and h == 3: return True
    if x < 78 and h == 3: return False
    if x >= 78 and h < 3: return False
    else:
        if h % 2 == 0:
            return any([f(x + 1, h + 1), f(x + 4, h + 1), f(x * 4, h + 1)])
        return all([f(x + 1, h + 1), f(x + 4, h + 1), f(x * 4, h + 1)])

for x in range(1, 37):
    if f(x, 1):
        print(x)
# 5 