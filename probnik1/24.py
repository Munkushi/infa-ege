f = open("probnik1/24.txt").readline()
#cnt = 0

with open("probnik1/24.txt") as m:
    for line in m:
        cnt = 0
        for j in range(len(line) - 2):
            if line[j] == "O" and line[j+2] == "E":
                cnt +=1
print(cnt)