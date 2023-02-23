m =-999999
z = 999999


for i in range(1, 101):
    a = bin(i)[2:]
    a = a[::-1]
    r = int(a, 2)
    if r == 11:
        m = max(a, z)
        mm = min(a, m)
print(mm + m)


# error gde to 