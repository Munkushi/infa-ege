from itertools import *

a = list(product("ТУМАН", repeat = 4))
count = 0


for i in a:
    if i.count("А") <= 3:
        count += 1


print(count)