# x341y v 11 + 56x1y v 19

for x in "0123456789A":
    for y in "0123456789A":
        s = int(x + "341" + y, 11) + int("56" + x + "1" + y, 19)
        if s % 305:
            print(s // 305)

# 2778