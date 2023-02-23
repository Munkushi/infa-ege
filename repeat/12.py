from itertools import *

a = list(product("КАРЕТ", repeat = 4))
cnt = 0

for i in a:
    if i[0] != "Т" and (i.count("Е") >= 1 or i.count("А") >= 1):
        cnt += 1

print(cnt)

# answer 446