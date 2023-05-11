for x in "0123456789ABCDE":
    s = int(f"97531{x}19", 15) + int(f"3{x}519", 15)
    if s % 11 == 0:
        print(s // 11)