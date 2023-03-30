def f(x, h):
    if x >= 68 and (h == 3 or h == 5): return True
    elif x > 68 and h < 5: return False
    elif x < 68 and h == 5: return False
    else:
        if h % 2 == 0:
            return any([f(x + 1, h + 1), f(x * 5, h + 1), f(x + 4, h + 1)])
        return all([f(x + 1, h + 1), f(x * 5, h + 1),  f(x + 4, h + 1)])
        

def f1(x, h):
    if x >= 68 and h == 3: return True
    elif x > 68 and h < 3: return False
    elif x < 68 and h == 3: return False
    else:
        if h % 2 == 0:
            return any([f1(x + 1, h + 1), f1(x * 5, h + 1), f1(x + 4, h + 1)])
        return all([f1(x + 1, h + 1), f1(x * 5, h + 1), f1(x + 4, h + 1)])        

for x in range(1, 67):
    if f(x, 1):
        print(x)
print()

for x in range(1, 67):
    if f1(x, 1):
        print(x)
# answer 8