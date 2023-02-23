for i in range(1, 100):
    n = i*"9"
    while ("444" in n) or ("999" or n):
        if ("444" in n):
            n = n.replace("444", "9", 1)
        elif ("999" or n):
            n = n.replace("999", "44", 1)
    
print(n)