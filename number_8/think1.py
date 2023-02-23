from itertools import *

a = list(permutations("ВЬЮГА", 5))
count = 0

for i in a:
    if i[0] != "Г" and "ЮГ" not in "".join(i) and "АГ" not in "".join(i):
        count += 1

print(count)