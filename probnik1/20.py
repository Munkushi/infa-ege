def f(x, y, h):
    if h == 4 and x + y >= 52: 
        return 1
    elif h == 4 and x + y < 52:
        return 0
    elif x + y >= 52 and h < 4:
        return 0
    else:
        if h % 2 != 0: # определить кто ходит по четности
            return f(x + 2, y, h + 1) or f(x, y + 2, h + 1) or f(x * 3, y, h + 1) or f(x, y * 3, h + 1) # win
        else:
            return f(x + 2, y, h + 1) and f(x, y + 2, h + 1) and f(x * 3, y, h + 1) and f(x, y * 3, h + 1) # lose

for x in range(1, 52):
    if f(x, 5, 1) == 1:
        print(x)
    
# 54 answer