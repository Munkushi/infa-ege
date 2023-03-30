
x = 7
n = "*" + x * "B" +  x* "A" + "*"
while ("**" not in n):
    if ("*AA" in n):
        n = n.replace("*AA", "A*A")
    else:
        n = n.replace("*A", "C*")
        n = n.replace("*B", "B*")
        n = n.replace("*BBB", "AC*A")
    #if n.count("A") == 5 and n.count("B") == 7:
print(n, n.count("C"))