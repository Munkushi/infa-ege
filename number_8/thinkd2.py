from itertools import *

a = list(permutations("ЛОЖКАРЬ", 7))
cnt = 0

for i in a:
    if i[0] != "Ь" and "ЬЖ" not in "".join(i) and "ЬА" not in "".join(i) and "ЬР" not in "".join(i):
        cnt += 1

print(cnt)