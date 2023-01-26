def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return 2 * f(n-1) + (n - 2) * f(n-2)

print(f(6))
# 142
