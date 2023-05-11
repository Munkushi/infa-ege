f = open("number_17/dosrok.txt").readlines()
f = [int(_) for _ in f]

cnt = 0
# 115
z = []
# for i in f:
#     if len(str(i)) == 3 and str(i)[-1] == "5":
#         z.append(i)

# print(min(z))
mn = 2000000
for i in range(len(f) - 1):
    if ((len(str(f[i])) == 3 and len(str(f[i + 1])) != 3) or (len(str(f[i])) != 3 and len(str(f[i + 1])) == 3)) and ((f[i] + f[i + 1]) % 115 == 0):
        cnt += 1
        mn = min(f[i] + f[i + 1], mn)

print(cnt, mn)