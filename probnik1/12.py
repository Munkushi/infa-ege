x = 7
n = "*" + x * "B" +  x * "A" + "*"
while ("**" not in n):
    if ("*AA" in n):
        n = n.replace("*AA", "A*A", 1)
    else:
        n = n.replace("*A", "C*", 1)
        n = n.replace("*B", "B*", 1)
        n = n.replace("*BBB", "AC*A", 1)
    #if n.count("A") == 5 and n.count("B") == 7:
print(n, n.count("C"), n.count("A"), n.count("B"))