z = open("number_17/17_6.txt").readlines()
z = [int(_) for _ in z]

count = 0
max_ = 0

for i in range(len(z) - 2):
    if (z[i]**2 + z[i+1]**2 > z[i+2]**2) and (z[i]**2 + z[i+2]**2 > z[i+1]**2) and (z[i+1]**2 + z[i+2]**2 > z[i]**2):
        count += 1
        max_ = max(max_, z[i]+z[i+1]+z[i+2])

print(count, max_)

# answer 5539 29451