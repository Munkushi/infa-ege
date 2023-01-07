n = 455 * "5"

while ("555" in n) or ("333" in n):
    if ("555" in n):
        n = n.replace("555", "3", 1)
    elif ("333" in n):
        n = n.replace("33", "535", 1)

print(n)

# 4778320
# 35535