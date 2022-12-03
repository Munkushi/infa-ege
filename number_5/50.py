m = []

for n in range(1, 100):
    new = bin(n)[2:]
    new = str(new)
    if n % 2 == 0:
        new = "1" + new + "0"
    else:
        new = "11" + new + "11"
    r = int(new, 2)
    if r > 52:
        m.append(r)
    

print(m)
 

# answer 56
