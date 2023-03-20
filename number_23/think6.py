def f(n):
    if n <= 13:
        return 2 * n * n + 4* n * n + 3
    elif n > 13 and n % 7 == 0:
        return f(n - 1) + n * n  + 23
    elif n > 13 and n % 7 != 0:
        return f(n - 2) + n - 18

cnt = 0
for n in range(1, 1001):
    flag = 1
    num = str(f(n))
    for i in num:
        if int(i)  % 2 != 0:
            flag = 0
    if flag == 1:
        cnt += 1

print(cnt)

# 18