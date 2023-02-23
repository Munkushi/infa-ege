from itertools import *

a = list(product("КОЛЕС", repeat = 6))
cnt = 0

for i in a:
    if (i.count("К") + i.count("Л") + i.count("C")) >= 3:
        cnt += 1

print(cnt)