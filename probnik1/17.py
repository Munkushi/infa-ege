f = open("probnik1/17.txt").readlines()
f = [int(_) for _ in f]


# -9984
cnt = 0

maxx = 999
for i in range(len(f) - 1):
    if f[i] > f[i+1] and str(f[i+1])[-1] == "4" and (f[i] ** 2 + 2*f[i]*f[i+1] + f[i+1]**2) < (-9984 ** 2):
            cnt += 1
            maxx = max(maxx, f[i] ** 2 + 2*f[i]*f[i+1] + f[i+1]**2)