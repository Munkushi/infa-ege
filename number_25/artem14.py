"""
ДЗ\отработка

Task 9

Пусть M— сумма минимального и максимального натуральных делителей целого числа, не считая единицы и самого числа.  
Если таких делителей у числа нет, то считаем значение M равным нулю.

Напишите программу, которая перебирает целые числа, большие 452021, в порядке возрастания и ищет среди них такие,  
для которых значение M при делении на 7 даёт в остатке 3. Вывести первые 5 найденных чисел и соответствующие им  
значения M.

Формат вывода: для каждого из 5 таких найденных чисел в отдельной строке сначала выводится само число, 
затем—  значение М. Строки выводятся в порядке возрастания найденных чисел.

Например, для числа 20 М=2+10=12, остаток при делении на 7 не равен 3; для числа 21
 М=3+7=10,остаток при делении на 7 равен 3.

 Answer:
452025 150678
452029 23810
452034 226019
452048 226026
452062 226033
"""

n = 0
x = 452021

while n < 5:
    x += 1
    for i in range(2, x // 2 + 1):
        if x % i == 0:
            min_d = i
            max_d = x / i # как ты до этого дошел
            break
    m = min_d + max_d 
    if m % 7 == 3:
        print(x, round(m))
        n += 1