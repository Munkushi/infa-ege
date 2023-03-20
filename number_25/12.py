def p(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def solve():
    for x in range(4567890, 4567990 + 1):
        if p(x):
            print(x)

solve()


# answers
# 4567891
# 4567907
# 4567919
# 4567931
# 4567963
# 4567967
# 4567973
# 4567987