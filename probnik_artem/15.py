"""
x&39 = 0 \/ (x&11 = 0 → x&A ≠ 0)
"""

def f(a, x):
    return ((x & 39) == 0) or (((x & 11) == 0) <= ((x & a) != 0))

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(a, x) == False:
            flag = False
            break
    if flag == True:
        print(a)