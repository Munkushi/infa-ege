def f(x, y, h):
    if h == 3 and x + y >= 231: # h = количество ходов для вина
        return 1
    elif h == 3 and x + y < 231:
        return 0
    elif x + y >= 231 and h < 3:
        return 0
    else:
        if h % 2 == 0: # определить кто ходит по четности
            return f(x + 1, y, h + 1) + f(x, y + 1, h + 1) + f(x * 2, y, h + 1) + f(x, y * 2, h + 1) # win
        else:
            return f(x + 1, y, h + 1) + f(x, y + 1, h + 1) + f(x * 2, y, h + 1) + f(x, y * 2, h + 1) # lose

for x in range(1, 214):
    if f(x, 17, 1) == 1:
        print(x)
    
# 54 answer