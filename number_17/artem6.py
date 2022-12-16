z = open("number_17/17_3.txt").readlines()
z = [int(_) for _ in z]

count = 0
max_ = 0

for i in range(len(z) - 1):
    if (z[i] + z[i+1] > z[i+2]) or (z[i] + z[i+2] > z[i+1]) or (z[i+1] + z[i+2] > z[i]):
        count += 1
        max_ = max(max_, z[i]+z[i+1]+z[i+2])

print(count, max_)

