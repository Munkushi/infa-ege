# n = "2" + x*"3"
for z in range (1, 100):
    n = "2" + z*"3"

    while ("23" in n) or ("2" in n):
        if ("23" in n):
            n = n.replace("23", "332", 1)
        elif ("2" in n):
            n = n.replace("2", "3", 1)

    if 10 <= len(n) <= 99:
        print(z)
        
# answer = 49