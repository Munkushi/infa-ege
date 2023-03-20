f = open("number_24/think1.txt").readline()

b = "B"

while b + "B" in f:
    b += "B"

print(len(b))