
a = {0: "Л", 1: "Н", 2: "О", 3: "С"}
count = 0
for i in range(0, len(a)):
    for j in range(0, len(a)):
        for g in range(0, len(a)):
            for m in range(0, len(a)):
                for n in range(0, len(a)):
                    count += 1
                    if count == 1020:
                        print(a[i], a[j], a[g], a[m], a[n], end=" ")

# СССОС