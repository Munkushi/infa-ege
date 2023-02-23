from itertools import *

a = list(product("КУРАГ", repeat = 6))
cnt = 0


for i in a:
    if (i.count("К") + i.count("Р") + i.count("Г")) >= 3: 
        cnt += 1


print(cnt)
# answer 12825