from itertools import *

a = list(product("МЕТА", repeat = 4))
count = 0


for i in a:
    if i.count("Е") >= 1:
        count += 1

print(count)

# 175