n = 80 * "1"


while ("11111" in n):
    if ("11111" in n):
        n = n.replace("111", "2", 1)
        n = n.replace("222", "1", 1)
print(n)