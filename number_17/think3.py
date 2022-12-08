count = 0
nums = []


for i in range(65789, 101235):
    if (i % 15 == 0 and i % 13 == 0) and (i % 8 != 0 and i % 11 != 0) and (((i % 100) // 10) in [2, 9]):
        nums.append(i)