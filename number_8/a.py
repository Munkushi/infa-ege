from itertools import *

a = list(product("АКЛМНЯ", repeat = 5))

cnt = 0

for i in a:
    cnt += 1
    if i[0] == "К" and i[1] == "М":
        print(cnt, i)
        break