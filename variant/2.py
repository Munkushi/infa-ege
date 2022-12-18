def f(x, y, z, w):
    return (not (not y or x) or (not z or w) or not z)


print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if f(x, y, z, w) == False:
                    print(x, y, z, w)