from itertools import *

a = list(permutations("РУБАНОК", 5))
# если слова повторяются 1 раз - permutations
cnt = 0

for i in a:
    if i[0] != "О" and "АО" not in "".join(i):
        cnt += 1

print(cnt)
# 1920