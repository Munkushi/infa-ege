f = open("number_24/dosrok.txt").readline()

m = ("QQ", "RR", "SS", "QR", "QS", "RQ", "RS", "SQ", "SR")

cnt = 0
mx_c = 0
for i in range(len(f) - 1):
    cnt += 1
    if (str(f[i]) + str(f[i+1])) in m:
        if mx_c < cnt:
            mx_c = cnt
        cnt = 0
print(mx_c)

# 544