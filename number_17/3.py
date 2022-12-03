file_ = open("number_17/17_3.txt").readlines()

file_ = [int(_) for _ in file_]
count = 0
summ = []

for m in file_:
    if m % 2 == 0:
        summ.append(m)

sum_ = sum(summ) / len(summ)
# print(sum(summ) / (len(summ)+1))

max_s = 0
for i in range(len(file_)-1):
    if (file_[i] % 3 == 0 or file_[i+1] % 3 == 0) and (file_[i] < sum_ or file_[i+1] < sum_):
        count += 1
        max_s = max(max_s, file_[i]+file_[i+1])

print(count, max_s)

# 2288 14875