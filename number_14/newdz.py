n = (41 * (17 ** 34)) + (12 * (71 ** 103)) - (22 * (14 ** 34)) + (56 * (2 ** 11)) + 6786
x1 = ""

while n > 0:
    x1 += str(n % 7)
    n //= 7

print(x1)
