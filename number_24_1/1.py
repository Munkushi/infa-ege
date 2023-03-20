f = open("number_24_1/1.txt").readline()
ln = 1
mx = 1

for i in range(len(f) - 1):
    if f[i] != f[i+1]:
        ln += 1
        if mx < ln:
            mx = ln
    else:
        ln = 1
print(mx)

# 42