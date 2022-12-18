a = {0: "А", 1: "О", 2: "У"}
count = 0

for i in range(0, len(a)):
    for m in range(0, len(a)):
        for x in range(0, len(a)):
            for y in range(0, len(a)):
                for mm in range(0, len(a)):
                    count += 1
                    if count == 210:
                        print(a[i], a[m], a[x], a[y], a[mm], end=" ")

# УОУАУ