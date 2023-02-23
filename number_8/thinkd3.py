from itertools import *

a = list(permutations("ОРЕЛ", 5))
cnt = 0

for i in a:
    if "ОЕ" not in "".join(i) and "ЕО" not in "".join(i) and "ОО" not in "".join(i):
        cnt += 1
        print(i)

print(cnt)