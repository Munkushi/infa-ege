f = open("number_24_2/1.txt").readline()
mx = 0
ln = 0

for i in range(len(f) - 1):
    if f[i] == "X" and f[i + 1] == "Z" and f[i + 2] == "Z" and f[i + 3] == "Y":
        if ln > mx:
            mx = ln
        ln = 1
    else:
        ln += 1
if mx < ln:
    mx = ln
print(mx)

# 1711