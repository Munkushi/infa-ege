"""
Найди длину самой длинной подцепочки, состоящей 
из символов Z
"""

f = open("number_24/1.txt").readline()

a = "Z"
while a + "Z" in f:
    a += "Z"

print(len(a))