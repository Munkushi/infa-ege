z = open("number_17/17_3.txt").readlines()
z = [int(_) for _ in z]

count = 0
max_ = 0
summ = sum(z)
lenn = len(z)
sr = summ / lenn

for i in range(len(z) - 1):
    if (z[i] % 5 == 0 or z[i+1] % 5 == 0) and (z[i] < sr or z[i+1] < sr):
        count += 1
        max_ = max(max_, z[i]+z[i+1])


print(count, max_)

# answer 1533 14932