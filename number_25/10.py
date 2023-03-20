def p(x):
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def m():
    for i in range(345678, 345698+1):
        cnt = 0
        z = []
        for m in range(1, int(i**0.5)+1):
            if i % m == 0:
                cnt += 2
                z.append(m)
                z.append(i // m)
                # print(i)
        if len(set(z)) == 6:
            print(sorted(z))

m()

# answers
# [1, 2, 4, 86423, 172846, 345692]
# [1, 11, 121, 2857, 31427, 345697]