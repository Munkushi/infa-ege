from itertools import *

a = list(product("ГЕРОН", repeat = 4))
count = 0


for i in a:
    if i[0] != "Н" and (i.count("Е") >= 1 or i.count("О") >= 1):
        count += 1

print(count)