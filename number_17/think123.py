f = [int(i) for i in open("").readlines()]
s_a = sum(f) // len(f) # среднее ариф
cnt = 0

for i in range(len(f) - 1):
    if (f[i] <= s_a or f[i+1] <= s_a) and ("3" not in str(f[i])or "3" not in str(f[i+1])):
        cnt += 1
        m = max(m, sum(f[i], f[i+1]))

print(cnt, m)