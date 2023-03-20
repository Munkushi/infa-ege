def p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def solve():
    for xx in range(345123, 345156 + 1):
        cnt = 0
        z = []
        for m in range(1, int(xx ** 0.5)):
            if xx % m == 0:
                z.append(m)
                z.append(xx // m)
        if len(set(z)) == 4:
            print(sorted(z))
                       

solve()


# answers
# [1, 269, 1283, 345127]
# [1, 71, 4861, 345131]
# [1, 5, 69029, 345145]
# [1, 2, 172573, 345146]
# [1, 7, 49307, 345149]
# [1, 5, 69031, 345155]