from itertools import *

a = list(product("ДОРФЕЙ", repeat = 5))
cnt = 0

for i in a:
    if i[0] != "Й" and i.count("Й") <= 1 and i[-1] != "Й" and "ЕЙ" not in "".join(i) and "ЙЕ" not in "".join(i):
        cnt += 1

print(cnt)

# 4325