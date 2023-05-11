from itertools import *

a = list(product("АВЛОР", repeat = 4))
cnt = 0

for i in a:
    cnt += 1
    if i[0] == "Л":
        print(cnt, i)
        break