from itertools import *

a = list(permutations("ДОЛЬКА", 6))
cnt = 0
for i in a:
    if i[0] != "Ь" and ("ОЬ" not in "".join(i) and "АЬ" not in "".join(i)):
        cnt += 1

print(cnt)
# 360