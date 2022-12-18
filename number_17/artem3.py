z = open("number_17/17_3_3.txt").readlines()
z = [int(_) for _ in z]

count = 0
max_ = 0
# сумма нечётна, а произведение делится на 5
for i in range(len(z) - 1):
    for j in range(i + 1, len(z)):
        if (z[i] + z[j]) % 2 != 0 and (z[i] * z[j]) % 5 == 0:
            count += 1
            max_ = max(max_, z[i] + z[j])


print(count, max_)