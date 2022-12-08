n = "*" + 27 * "1" + 45 * "2" + 18 * "3"

while ("*1" in n) or ("*2" in n) or ("*3" in n):
    if ("*1" in n):
        n = n.replace("*1", "22*", 1)
    elif ("*2" in n):
        n = n.replace("*2", "2*1", 1)
    elif ("*3" in n):
        n = n.replace("*3", "1*", 1)

n = n.replace("*", "", 1)
n = sum([int(_) for _ in n])
print(n)

# answer = 396

# -------------------------------------------------- Второй способ решения

s = list(27 * "1" + 45 * "2" + 18 * "3")
summ = 0
while s != []:
    a = s.pop()
    if a == "1":
        summ += 4
    if a == "2":
        summ += 6
    if a == "3":
        summ += 1
print(summ)