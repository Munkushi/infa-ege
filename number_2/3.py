def f(a, b, c, d):
    return (a or not b) == (not(b) or (not(c == (d and a))))

print("a b c d")
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                if f(a, b, c, d) == 0:
                    print(a, b, c, d)