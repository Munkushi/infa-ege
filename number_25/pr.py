def num1():
    for i in range(1, 1000000):
        s = str(i)[1:] == "14" and str(i)[3] == "4"
        if s and s % 217 == 0:
            print(s)