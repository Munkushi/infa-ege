def f(x, h):
    if x >= 68 and h == 4: return 1
    elif x > 68 and h < 4: return 0
    elif x < 68 and h == 4: return 0
    else:
        if h % 2 != 0:
            return f(x + 1, h + 1) or f(x * 5, h + 1) or f(x + 4, h + 1)
        else:
            return f(x + 1, h + 1) and f(x * 5, h + 1) and f(x + 4, h + 1)
        
for x in range(1, 67):
    if f(x, 1) == 1:
        print(x)

# answers 9 12