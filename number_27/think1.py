with open("") as f:
    n = int(f.readline())
    summ = 0
    min_r = 10 ** 6
    for i in range(n):
        data = list(map(int, f.readlines().split()))
        summ += max(data)
        if data[0] - data[1] % 4 != 0:
            min_r = min(min_r, data[0] - data[1])
    if summ % 4 == 0:
        summ -= min_r

print(summ)