for i in range(1, 100):
    m = ">" + 39*"0" + i * "1" + 39 * "2"

    while (">1" in m) or (">2" in m) or (">0" in m):
        if (">1" in m):
            m = m.replace(">1", "22>", 1)
        elif (">2" in m):
            m = m.replace(">2", "2>", 1)
        elif (">0" in m):
            m = m.replace(">0", "1>", 1)
    if 10 <= len(m) <= 99:
        print(i)