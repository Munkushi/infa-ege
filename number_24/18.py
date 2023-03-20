f = open("number_24/17.txt").readlines()
cnt = 0

for i in f:
    if i.count("DA") > 3:
        cnt += 1

print(cnt)

# 56