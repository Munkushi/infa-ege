count = 0

for x1 in range(1, 100000):
    x = x1
    s = 14 * (x // 10)
    n = 1
    while s < 300:
        s = s + 300
        n = n * 2
    if n > 550:
        count += 1

print(n, x1)
# print(n)