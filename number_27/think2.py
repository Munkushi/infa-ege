with open("") as f:
    n = int(f.readline())
    a = list(map(int, f.readlines()))
    cnt = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (a[i] + a[j]) % 2 == 0:
                cnt += 1

print(cnt)
# B
with open("") as f:
    n = int(f.readline())
    a = list(map(int, f.readlines()))
    cnt = 0
    k_ch, k_nech = 0
    for i in range(n - 1):
        if a[i] % 2 == 0:
            k_ch += 1
        else:
            k_nech += 1
        

print(k_ch * (k_ch -1 ) // 2 + k_nech*(k_nech - 1) // 2)