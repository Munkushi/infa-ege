f = open("number_24/24_Решу_Егэ_Ч1.txt").readline()

a = "Y"

while a + "Y" in f:
    a += "Y"

print(len(a))