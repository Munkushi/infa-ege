f = int("10000", 8)
e = int("77777", 8)

count = 0

for i in range(f, e+1):
    s = str(oct(i))[2:]
    sx = s.count("6")
    if sx == 1:
        if (s[-1] == "6") and (int(s[-2]) % 2 == 0):
            count += 1
        elif (s[0] == "6") and (int(s[1]) % 2 == 0):
            count += 1
        elif (s[2] == "6") and (int(s[1]) % 2==0 and int(s[3]) % 2 ==0): 
            count += 1
        elif (s[3] == "6") and (int(s[2]) % 2==0 and int(s[4]) % 2 ==0): 
            count += 1
        elif (s[1] == "6") and (int(s[0]) % 2==0 and int(s[2]) % 2 ==0): 
            count += 1
print(count)

# 2961