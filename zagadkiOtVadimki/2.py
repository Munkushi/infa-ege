filee = open("zagadkiOtVadimki/17.txt").readlines()
filee = [int(_) for _ in filee]
count = 0
z = []

for i in range(len(filee)):
    if (str((filee[i] % 4)) == str((filee[i] % 9))) and ((int(filee[i]) % 13 == 0) or (int(filee[i]) % 74 == 0) or (int(filee[i]) % 51 == 0)):
        count += 1
        z.append(filee[i])
    

print(z)
print(count, min(z))
