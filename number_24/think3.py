f = open("number_24/think3.txt").readline()
cnt = 0

for i in f:
    ff = 0
    for j in range(len(i) - 3):
        if i[j] == "D" and i[j+1] == "O" and i[j+2] == "P" and ff == 0:
            ff = 1
            cnt += 1

print(cnt)
