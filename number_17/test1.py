count = 0
summ = 0

for i in range(118, 4093):
    if (i % 16 == 0 or i % 16 == 11) and (i % 3 != 0 or i % 8 == 0):
        count += 1
        summ += i

print(summ, count)

