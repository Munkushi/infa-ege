f = open("number_24/17.txt").readlines()
cnt = 0


# for i in range(len(f)):     
#    if i.count(f"ZY{f[i+1]}") > 0:
#         cnt += 1

# print(cnt)
m_c = 0
num = 0
for i in range(len(f)):
    c = f[i][::-1].count("YZ")
    if m_c < c:
        m_c = c
        num = i + 1