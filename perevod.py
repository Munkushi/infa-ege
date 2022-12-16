x = 212331232
x1 = ""

while x > 0:
    x1 = str(x % 5)
    x //= 5

x1 = x1[::-1]
print(x1)