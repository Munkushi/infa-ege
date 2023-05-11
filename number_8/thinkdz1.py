cnt = 0
for i in range(1_000_00, 1_000_000, 5):
    m = set()
    if ((int(str(i)[0]) + int(str(i)[1])) % 2 != 0) and ((int(str(i)[1]) + int(str(i)[2])) % 2 != 0) and ((int(str(i)[2]) + int(str(i)[3])) % 2 != 0) and ((int(str(i)[3]) + int(str(i)[4])) % 2 != 0) and ((int(str(i)[4]) + int(str(i)[5])) % 2 != 0):
        m.add(int(str(i)[0]))
        m.add(int(str(i)[1]))
        m.add(int(str(i)[2]))
        m.add(int(str(i)[3]))
        m.add(int(str(i)[4]))
        m.add(int(str(i)[5]))
        print(m, i, len(m))
        if len(m) == 6:
            cnt += 1
print(cnt)