from itertools import *

count = 0
for i in product("12345", repeat=5):
    if i.count("1") == 3:
        count += 1

print(count)
# answer = 160