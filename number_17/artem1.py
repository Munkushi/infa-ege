z = open("number_17/17_1_1.txt").readlines()
z = [int(_) for _ in z]

count = 0

m = 0
for i in range(len(z)-1):
    for j in range(i + 1, len(z)):
        if ((z[i]-z[j]) % 2 == 0) and (z[i] % 19 == 0 or z[j] % 19 == 0):
            count += 1
            m = max(m, z[i]+z[j])

print(count, m)

# answer 2551262 19994