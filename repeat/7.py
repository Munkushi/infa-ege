from itertools import *

a = list(product("АПРСУ", repeat = 5))
cnt = 1

for i in a:
    if "".join(i) == "УАПАП":
        print(cnt)
    cnt += 1

# answer 2527
