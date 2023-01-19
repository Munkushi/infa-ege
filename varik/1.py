n = 27

x1 = ""
while n > 0:
    x1 += str(n % 14)
    n //= 14 + int(x1)

print(x1)