from itertools import *

a = list(product("АБВГД", repeat = 5))
cnt = 0
for i in a:
    cnt += 1

print(cnt)

# 3125