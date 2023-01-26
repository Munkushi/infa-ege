def f(x, y, w, z):
    return ((not x or y) and (not y or w)) or (z == (x or y))


print("x y w z")
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if f(x, y, w, z) == False:
                    print(x, y, w, z)

# ywzx