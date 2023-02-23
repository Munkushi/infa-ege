from itertools import *

a = list(permutations("ДОЛИНА", 6))
cnt = 0


for i in a:
    if "АО" not in "".join(i) and "АИ" not in "".join(i) and "ОИ" not in "".join(i) and "ОА" not in "".join(i) and "ИА" not in "ДЛ".join(i) and "ДН" not in "".join(i) and "НД" not in "".join(i) and "НЛ" not in "".join(i) and "НЛ" not in "".join(i):
        cnt += 1

print(cnt)

# 72 ответ но у меня 184