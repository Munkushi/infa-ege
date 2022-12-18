a = {0: "А", 1: "К", 3: "Р", 4: "У"}
count = 0

for i in range(0, len(a)):
    for m in range(0, len(a)):
        for x in range(0, len(a)):
            for y in range(0, len(a)):
                for mm in range(0, len(a)):
                    count += 1
                    if i == 1:
                        print(count)

# 257