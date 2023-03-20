def f(x, y, h):
    if (h == 3 or h == 5) and x + y >= 77:
        return 1
    elif h == 5 and x + y < 77:
        return 0
    elif h < 5 and x + y >= 77:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 2, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)

def f1(x ,y, h):
    if h == 3 and x + y >= 77:
        return 1
    elif h == 3 and x + y < 77:
        return 0
    elif h < 3 and x + y >= 77:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, y, h + 1) or f(x * 2, y, h + 1) or f(x, y + 1, h + 1) or f(x, y * 2, h + 1)
        else:
            return f(x + 1, y, h + 1) and f(x * 2, y, h + 1) and f(x, y + 1, h + 1) and f(x, y * 2, h + 1)

for x in range(1, 69):
    if f(x, 8, 1) == 1:
        print(x)
print("--------")
for x in range(1, 69):
    if f1(x, 8, 1) == 1:
        print(x)

# 34
# вторая функция вообще юзлесс или какой то смысл есть, ответ то один получается