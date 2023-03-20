f = open("number_24_1/2.txt").readlines()
cnt = 0


for i in f:
    if i.count("A") > i.count("E"):
        cnt += 1

print(cnt)


# 485