count = 0

mx = 2357


for i in range(2358, 5690):
    i = str(i)
    if i.count("9") == 0 and i.count("8") > 0:
        if int(i[0]) * int(i[1]) * int(i[2]) * int(i[3]) > 28 and int(i) % 3 == 0:
            if mx < int(i):
                count += 1


print(count, int(i))