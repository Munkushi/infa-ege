import math

for i in range(1, 1000):
    n = ">" + 39 * "0" + i * "1" + 39 * "2"

    while (">1" in n) or (">2" in n) or (">0" in n):
        if (">1" in n):
            n = n.replace(">1", "22>", 1)
        elif (">2" in n):
            n = n.reaplce(">2", "2>", 1)
        elif (">0" in n):
            n = n.replace(">0", "1>", 1)
        # n = int(n)

        if (int(n) ** 0.5) % 2 == 0:
            print(n)

        # math.sqrt(int(n)).is_integer()