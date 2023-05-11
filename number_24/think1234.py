f = open("").readline().split("T")
m = ""
for i in f:
    if i.count("R") == 4:
        m = max(m, i, key = len)


print(len(m))