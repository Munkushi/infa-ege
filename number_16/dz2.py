def f(n):
    if n > 27:
        return n * n * n + 4 *n * n + 3
    elif n <= 27 and n % 8 == 0:
        return 4 * f(2 * n + 1) + 2 * f(n + 4)
    elif n <= 27 and n % 8 != 0:
        return 2* f(n + 3) + f(n + 9) + f(n + 9)

for x in range(1, 501):
    z = str(f(x))
    z += z 
    if z == "27":
        print(z)