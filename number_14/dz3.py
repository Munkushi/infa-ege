z = 32 ** 1523 - 4 ** 345 + 2 ** 511 - 152
z = bin(z)[2::]


zero = z.count("0")
one = z.count("1")
print(zero, one, one - zero)
print(z)
