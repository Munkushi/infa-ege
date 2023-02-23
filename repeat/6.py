from itertools import *

a = list(product("ВИШНЯ", repeat=6))
cnt = 0

for i in a:
    if i[0] != "Ш" and i[-1] != "И" and i[0] != "Я" and i.count("В") <= 1:
        cnt += 1

print(cnt)


# answer = 4352