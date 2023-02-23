k = []

for i in range(4, 1010):
    a = bin(i)[2:]
    if a.count("1") > a.count("0"): 
        a += "0"
    else: 
        a += "1"
    a = list(a)
    if len(a) % 2 == 0:
        a.pop(len(a) // 2)
        a.pop(len(a) // 2)
    else:
        a.pop(len(a) // 2)
        a.pop(len(a) // 2)
        a.pop(len(a) // 2)
    a = int("".join(a), 2)
    print(a)
    if a % 2 == 0 and a in range(48, 100):
        k.append(a)

print(len(set(k)))

# answer 8