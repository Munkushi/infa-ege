from itertools import *

a = list(product("ДЕКОР", repeat=4))
cnt = 0

for i in a:
    cnt += 1
    if i[0] == "О":
        print(cnt)

# 376