def f(x, y, z, w):
    return not ((not z or y) and (x or w)) or ((z == w) or (y and (not x)))

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)