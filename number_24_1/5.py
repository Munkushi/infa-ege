f = open("number_24_1/3.txt").readline()
maxx = 0
max_l = ""
alp = set(f)

for i in alp:
    c = f.count("E" + i)
    if c > maxx:
        maxx = max(maxx, c)
        max_l = i

print(max_l)

# Y