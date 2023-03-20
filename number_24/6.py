f = open("number_24/5.txt").readlines()
cnt = 0

for i in f:
    ff = 0
    for j in range(len(i) - 2):
        if i[j] == "D" and i[j+2] == "G" and ff == 0:
            ff = 1
            cnt += 1

print(cnt)

# 809