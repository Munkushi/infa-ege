from itertools import *

count = 0

for i in product("ЕИКПРС", repeat = 4):
    s = "".join(i)
    if i[0] == "Р" and i[1] == "И":
        print(count)
print(count)

# не работает