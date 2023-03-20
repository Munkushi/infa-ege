f = open("number_24/4.txt").readlines()

ln = 1
mx = 1
cnt = 0

for i in f:
    if i.count("Y") > i.count("Z"):
        cnt += 1

print(cnt)

# 506