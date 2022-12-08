file_ = open("number_17/ht4.txt").readlines()
m = [int(_) for _ in file_]
count = 0
s = 0


for i in (len(m)-1):
    if str((m[i])[-1]) == "4" or str((m[i+1])[-1]) == "4":
        i = int(i)
        count += 1
        s = max(s, m[i]+m[i+1])

print(count, s)

# ne poshlo