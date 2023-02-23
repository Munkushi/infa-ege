from itertools import *

a = list(permutations("БАНЩИК", 6))
count = 0

for i in a:
    if i[0] != "Н" and "ИА" not in "".join(i):
        count += 1

print(count)