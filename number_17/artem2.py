z = open("number_17/17_2.txt").readlines()
z = [int(_) for _ in z]

count = 0
max_num = 0

for i in range(len(z) - 1):
    for j in range(i + 1, len(z)):
        if z[i] * z[j] % 62 == 0:
            count += 1
            max_num = max(max_num, z[i] + z[j])

print(count, max_num)

# answer  2284645 19920