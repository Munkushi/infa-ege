filee = open("number_17/17_1.txt").readlines()
filee = [int(_) for _ in filee]

count = 0
d = 160
max_s = 0


for i in range(len(filee)-1):
    for m in range(i+1, len(filee)):
        if (filee[i] % d != filee[m] % d) and (filee[i] % 7 == 0 or filee[m] % 7 == 0):
            count += 1
            max_s = max(max_s, filee[i]+filee[m])


print(count, max_s)

# 12749665 19989