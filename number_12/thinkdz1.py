s = "1" + 35*"5"

while ("15" in s) or ("1" in s):
    if ("15" in s):
        s = s.replace("15", "55551", 1)
    elif ("1" in s):
        s = s.replace("1", "55", 1)

print(s.count("5"))