def f(a: int, b: int) -> int:
    if a > b:
        return f(a - 1, b)
    elif a <= b and b > 0:
        return f(f, b - 1) + a

for a in range(2000):
    for b in range(2000):
        if f(a, b) == 1224892:
            print(a)