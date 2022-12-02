m = []

for n in range(2, 100):
    b = bin(n)[2:]
    b = str(b)
    b = b + str(b)[-2] 
    b = b + str(b)[1]
    int_b = int(b, 2)
    if int_b > 150:
        print(n)

# 38