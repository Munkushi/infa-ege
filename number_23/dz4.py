import sys

sys.setrecursionlimit(15000)


def f(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    return f(x - 3, y) + f(x // 4, y)
print(f(1, 13) * f(13, 69))