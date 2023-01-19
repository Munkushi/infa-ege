num = 280 * "1"

while ("111" in num):
    if "111" in num:
        num = num.replace("11", "2", 1)
        num = num.replace("223", "3", 1)
        num = num.replace("331", "1", 1)

print(num)