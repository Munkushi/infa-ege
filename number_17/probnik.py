filee = open("number_17/17 (3).txt").readlines()
filee = [int(_) for _ in filee]

summ = 0
count = 0

for i in range(len(filee) - 1):
    for y in range(i+1, len(filee)):
        if (filee[i] + filee[y]) % 126 == 0:
            summ = max(summ, filee[i] + filee[y])
            count += 1

print(count, summ)
# 397339 19908