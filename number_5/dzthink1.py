cnt = 0
for i in range(1, 100):
    a = bin(i)[2:]
    if a % 2 == 0:
        a = str(a)
        a = "1" + a + "10"
    else:
        a = str(a)
        a = "11" + a + "0"
    r = int(a, 2)
    if r in range(456, 1891):
        cnt += 1

print(cnt)