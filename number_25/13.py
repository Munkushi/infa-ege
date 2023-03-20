def p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solve():
    cnt = 0
    mx = 0
    for x in range(125697, 190234 + 1):
        for i in range(1, int(x ** 0.5) + 1):
            if p(i) and p(x // i) and i * (x // i) == i and i != x // i:
                cnt += 1
                mx = max(mx, x)
    print(cnt, mx)


solve()