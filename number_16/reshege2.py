from itertools import *

count = 0

for i in product("ЛНРТ", repeat=5):
    count += 1
    if count == 150:
        print(i)
