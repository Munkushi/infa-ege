"""
HW

Task 13

Напишите программу, которая ищет среди целых чисел, принадлежащих числовому отрезку [489421; 489440], числа,  
имеющие ровно четыре различных натуральных делителя. Для каждого найденного числа запишите эти четыре делителя в 
четыре  соседних столбца на экране с новой строки. Делители в строке должны следовать в порядке возрастания.

Например, в диапазоне [12;14] ровно четыре различных натуральных делителя имеет число 14, поэтому для этого  
диапазона вывод на экране должна содержать следующие значения:

1 2 7 14

Ответ:
1 19 25759 489421
1 2 244711 489422
1 13 37649 489437
"""


# for i in range(489421, 489440 + 1):
#     k = 0
#     z = []
#     for j in range(1, int(i** 0.5) + 1):
#         if i % j == 0:
#             z.append(j)
#             z.append(i // j)
#             if len(z) > 4:
#                 break
#     if len(z) == 4:
#         print(z)


for i in range(489421, 489440 + 1):
    z = [int(j) for j in range(1, i + 1) if i % j == 0]
    if len(z) == 4:
        print(z)


# [1, 19, 25759, 489421]
# [1, 2, 244711, 489422]
# [1, 13, 37649, 489437]