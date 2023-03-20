"""
Отработка

Task 5

Пусть M(N)— произведение 5 наименьших различных натуральных делителей натурального числа N, не считая единицы. 
Если у числа N меньше 5 таких делителей, то M(N) считается равным нулю.

Найдите 5 наименьших натуральных чисел, превышающих 500_000_000, для которых0<M(N)<N. 
В ответе запишите найденные значения M(N) в порядке возрастания соответствующих им чисел N.

Ответ:
1008
1797092
48408867
1800
1156923
"""

big_n = 500_000_00
n = 0

while n < 5:
    big_n += 1
    divisors = set()
    for i in range(2, int(big_n ** 0.5) + 1):
        if big_n % i == 0:
            divisors.add(i)
            divisors.add(big_n // i)
    divisors = sorted(divisors)
    if len(divisors) >= 5:
        umn = divisors[0] * divisors[1] * divisors[2] * divisors[3] * divisors[4] 
    else:
        umn = 0
    if 0 < umn < big_n:
        n += 1
        print(umn)