f = open("number_24_2/3_3.txt").readline()

cnt = 0

# A, C, D, F и O. 
# solg + gl
# ca = "CA"
# co = "CO"
# da = "DA"
# do = "DO"
# fa = "FA"
# fo = "FO"
# while ca + "CA" in f:
#     ca += "CA"

# while co + "CO" in f:
#     co += "CO"

# while da + "DA" in f:
#     da += "CA"

# while do + "DO" in f:
#     do += "DO"

# while fa + "FA" in f:
#     fa += "FA"

# while fo + "FO" in f:
#     fo += "FO"

# print(len(ca), len(co), len(da), len(do), len(fa), len(fo))

# ya arab

# A, C, D, F и O

gl = ["A", "O"]
sg = ["C", "D", "F"]
cnt = 0
mx = 0
for i in range(0, len(f), 2): # 2
    if (f[i] in sg) and (f[i+1] in gl):
        cnt += 1
        if cnt > mx:
            mx = max(cnt, mx)
    else:
        cnt = 0

print(mx)

# 95