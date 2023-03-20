f = open("number_24/12.txt").readline()
# a = f.find("A")
# print(a)
# 90
m_c = 0
let = ""
alp = set(f)
for i in alp:
    c = f[f.find("A"+i) + 1:].count(i)
    # print(f[f.find("A") + 1:])
    # break
    if m_c < c:
        m_c = c
        let = i


print(m_c, let)


# E308