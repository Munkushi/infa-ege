f = int("1011", 2)
s = int("1011", 8)
count = 0
nums = []

for i in range(1000, 100001+1):
    if i % f == 0 or i % s == 0 and i % 250 == 0:
        count += 1
        nums.append(i)

print(count, min(nums))