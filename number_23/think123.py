def f(x, y):
    global a
    if y < 15: # количество команд
        return f(x + 4, y + 1) + f(x * 2 - 2, y + 1)
    if y > 15:
        return 0
    if y == 15:
        a.add(x)
        return 1 
a = set()
f(2, 0)
print(len(a))