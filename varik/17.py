filee = open("varik/17 (2).txt").readlines()
filee = [int(_) for _ in filee]

count = 0

minn = 0
for i in range(len(filee)-1):
    if (filee[i] > 9955 or filee[i+1] > 9955) and (filee[i] % 16 == 11 or filee[i+1] % 16 == 11):
        count += 1
        minn = min(minn, filee[i]+filee[i+1])

print(count, minn)