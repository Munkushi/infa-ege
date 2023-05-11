for i in range(100, 1000):
    i = str(i)
    st = int(i[0])+3
    sr = int(i[1])+6
    ml = int(i[2])+5
    num = []
    num.append(st)
    num.append(sr)
    num.append(ml)
    if sorted(num)==[5,10,14]:
        print(i)

# 780