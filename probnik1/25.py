for i in range(1120345, 11293400):
    if (i % 127 == 0) and str(i)[-2] == "45" and str(i)[4] == "3":
        print(i)