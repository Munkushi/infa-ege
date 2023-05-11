for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for p in range(22, 37):
        for q in range(32, 37):
            s = int(f"ALE{x}",p) + int("DANOV", q)
            if s % 2023 == 0:
                print(s // 2023)