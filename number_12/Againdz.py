n = 196 * "9"

while ("222222" in n) or ("99999" in n):
    if ("222222" in n):
        n = n.replace("222222", "9999", 1)
    elif ("99999" in n):
        n = n.replace("99999", "2", 1)
    

print(n)

# 229999