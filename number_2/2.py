def f(x, y, z, w):
    return (x and not y) == ((not ( z or (not w))) or (x and z))


print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if f(x, y, z, w) == 0:
                    print(x, y, z, w)

# w y x z