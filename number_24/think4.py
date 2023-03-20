f = open("number_24/think4.txt").readline()

maxx = 0
max_l = ""
alp = set(f)

for i in alp:
    c = f.count("B" + i)
    if c > maxx:
        maxx = max(maxx, c)
        max_l = i

print(max_l)