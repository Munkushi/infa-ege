f = open("probnik1/24.txt").readline()
cnt = 0

for i in range(len(f) - 2):
    if f[i] == "O" and f[i+2] == "E":
        cnt +=1
print(cnt)