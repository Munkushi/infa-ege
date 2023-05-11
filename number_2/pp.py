"""
Автомат получает на вход четырёхзначное число (число не может начинаться с нуля). По этому числу строится новое число по следующим правилам.

1.  Складываются отдельно первая и вторая, вторая и третья, третья и четвёртая цифры заданного числа.

2.  Наименьшая из полученных трёх сумм удаляется.

3.  Оставшиеся две суммы записываются друг за другом в порядке неубывания без разделителей.

 

Пример. Исходное число: 1982. Суммы: 1 + 9 = 10, 9 + 8 = 17, 8 + 2 = 10. Удаляется 10. Результат: 1017.

Укажите наибольшее число, при обработке которого автомат выдаёт результат 1315.

 

Примечание. Если меньшие из сумм равны, то отбрасывают одну из них.
"""

for i in range(1000, 10001):
    summ12 = int(str(i)[0]) + int(str(i)[1])
    summ23 = int(str(i)[1]) + int(str(i)[2])
    summ34 = int(str(i)[2]) + int(str(i)[3])
    z = []
    z.append(summ12)
    z.append(summ23)
    z.append(summ34)
    z = sorted(z)
    # print(z)
    if (str(z[1]) == "13") and (str(z[2]) == "15"):
        print(i)
        