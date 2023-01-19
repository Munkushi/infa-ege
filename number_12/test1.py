# num = 5*"6"
for i in range(48, 60):
    num = i*"6"
    while ("666" in num):
        if "666" in num:
            num = num.replace("666", "2", 1)
            num = num.replace("222", "6", 1)
        if num == "266":
            print(i)
# print(num)