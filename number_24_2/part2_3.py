f = open("number_24_2/3_2.txt").readline()

mx = 0
ln = 0

#print(len(f))
for i in range(1, len(f)):
    if ((f[i-1] == "K") and (f[i] == "L")) or ((f[i-1] == "L") and (f[i] == "K")):
        ln = 1
    else:
        ln += 1
        if ln > mx:
            mx = ln

print(mx)
# 2796