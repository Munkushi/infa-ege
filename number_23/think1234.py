def m(x, y, f):
    if x < y and f == 0:
        return m(x + 6, y, 0) + m(x + 3, y, 0) + f(x * 4, y, 1)
    if x < y and f == 1:
        return m(x + 6, y, 0) + m(x + 3, y, 0)