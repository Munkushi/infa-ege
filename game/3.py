f = open("game/1.txt").readline()


ln = 1
mx = 0
for i in range(1, len(f) - 1):
    if f[i] == "A" and f[i+1] == "Z":
        ln = 1
    else:
        ln += 1
        if ln > mx:
            mx = ln
            
print(mx)

