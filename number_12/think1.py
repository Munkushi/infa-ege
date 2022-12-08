num = "2" + 148*"5"

while ("25" in num) or ("3555" in num) or ("45" in num):
    if ("25" in num):
        num = num.replace("25", "4", 1)
    elif ("355" in num):
        num = num.replace("3555", "2", 1)
    elif ("45" in num):
        num = num.replace("45", "3", 1)

print(num)