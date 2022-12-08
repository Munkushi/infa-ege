count = 0
summ = 0

for i in range(5678, 11234+1):
   if i % 13 == 0 and i % 46 != 0:
       count += 1
       summ += i

print(count, summ)