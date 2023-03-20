f = open("number_24_1/1.txt").readline()

b = "B"

while b + "B" in f:
    b += "B"

print(len(b))

# 11