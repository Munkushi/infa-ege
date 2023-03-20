f = open("number_24_1/1.txt").readline()

ab = "AB"

cnt = 0
while ab + "B" in f:

    ab = "AB" + ab
    if ab + "B" in f:
        print(len(ab)) 
# print(ab)
    

a = "AB"
print("===================================")

while a + "A" in f:
    a = "AB" + a
    if a + "A" in f:
        print(len(a)) 

# print(len(ab), len(a))