import sys

sys.setrecursionlimit(10000)



def f(a: int, b: int) -> int:
    if a == 0 and b == 0:
        return 0
    if a > b:
        return f(a - 1, b) + b
    elif a <= b and b > 0:
        return f(a, b - 1) + a

for a in range(2000):
    for b in range(2000):
        print(f(a, b))