# ( (X & 50 ≠ 0) ∨ (X & S = 0)) → (X & 24 ≠ 0)) ∨ (X & S ≠ 0) ∨ (X & 33 = 0)
def f(x, a):
    return not (((x & 50 != 0) or (x & 5 == 0)) <= (x & 24 != 0)) or (x & a != 0) or ( x & 33 == 0)

for a in range(1, 100):
    flag = True
    for x in range(1, 100):
        if f(x, a) == False:
            flag = False
            break
    if flag == True:
        print(a)
        break

# print(33 * 4287)
print(oct(25 * 4287))