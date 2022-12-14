s = 187 * "7"

while ("77777" in s) or ("73" in s):
    if ("77777" in s):
        s = s.replace("77777", "73", 1)
    elif ("73" in s):
        s = s.replace("73", "7", 1)

print(s)