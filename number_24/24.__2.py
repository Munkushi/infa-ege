"""
В это файлике будут прорешиваться варианты заданич 24 с сайта Решу ЕГЭ
Часть 2
"""
#Task 1
"""
Текстовый файл 24_Решу_ЕГЭ_Ч2_1.txt содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки 
содержат только заглавные буквы латинского алфавита (ABC…Z). Определите количество строк, в которых буква E встречается чаще, чем буква A.

Ответ: 467

P.S. иногда код может быть очень коротким... если придумать как.
"""
# num = 0
# with open('24_Решу_ЕГЭ_Ч2_1.txt') as File:
#     for line in File:
#         num_E=0
#         num_A=0
#
    #     var1
    #     if line.count('E')>line.count('A'): num+=1
    #
    #     var 2
    #     for i in range(len(line)):
    #         if line[i]=='E':
    #             num_E+=1
    #         elif line[i]=='A':
    #             num_A+=1
    #     if num_E>num_A: num+=1
    # print(num)

#Task 2
"""
Текстовый файл 24_Решу_ЕГЭ_Ч2_2.txt содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, 
который чаще всего встречается в файле сразу после буквы A.

Ответ: G
"""
#решение через обычные массивы=коллекции

"""
попробовать записывать данные в строку, а затем считать количество букв в строке
"""
# with open('24_Решу_ЕГЭ_Ч2_2.txt') as File:
#     st = File.readline()
#
# letters = []
# count = []
#
# for i in range(len(st)-1):
#     if st[i]=='A':
#         if (st[i+1] in letters) == False:
#             letters.append(st[i+1])
#             count.append(1)
#             continue
#         num_element = letters.index(st[i+1])
#         count[num_element]+=1
#
# print(letters[count.index(max(count))])

#Task 3
"""
Текстовый файл 24_Решу_ЕГЭ_Ч2_2.txt содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, 
который чаще всего встречается в файле между двумя одинаковыми символами.

Answer: D
"""
#решение через обычные массивы=коллекции

# with open('24_Решу_ЕГЭ_Ч2_2.txt') as File:
#     st = File.readline()
#
# letters = []
# indexes = []
#
# for i in range(1,len(st)-1):
#     if st[i-1]==st[i+1]:
#         if (st[i] in letters) == False:
#             letters.append(st[i])
#             indexes.append(1)
#             continue
#         index = letters.index(st[i])
#         indexes[index]+=1
#
# index=indexes.index(max(indexes))
# print(letters[index])

#Task 4
"""
Текстовый файл 24_Решу_ЕГЭ_Ч2_2.txt содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, 
который чаще всего встречается в файле после двух одинаковых символов.

Answer: K
"""
# with open('24_Решу_ЕГЭ_Ч2_2.txt') as File:
#     st = File.readline()
#
# letters = []
# indexes = []
#
# for i in range(len(st)-2):
#     if st[i]==st[i+1]:
#         if (st[i+2] in letters) == False:
#             letters.append(st[i+2])
#             indexes.append(1)
#             continue
#         index = letters.index(st[i+2])
#         indexes[index]+=1
#
# index=indexes.index(max(indexes))
# print(letters[index])


#Task 5
"""
Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
Необходимо найти строку, содержащую наименьшее количество букв G (если таких строк несколько, надо взять ту, которая находится в файле раньше), 
и определить, какая буква встречается в этой строке чаще всего. Если таких букв несколько, надо взять ту, которая позже стоит в алфавите.

Пример. Исходный файл:
GIGA
GABLAB
AGAAA

В этом примере в первой строке две буквы G, во второй и третьей — по одной. Берём вторую строку, т.к. она находится 
в файле раньше. В этой строке чаще других встречаются буквы A и B (по два раза), выбираем букву B, т.к. она позже стоит в алфавите. 
В ответе для этого примера надо записать B.

Answer: T
"""

# with open('24_Решу_ЕГЭ_Ч2_3.txt') as File:
#     lines = [line for line in File]

#var1
# #записываю количество G в отдельный массив
# num_G = []
# for line in lines:
#     num_G.append(line.count('G'))
#
# #получаю строку с наименьшим количеством G
# line_min_G = lines[num_G.index(min(num_G))]

#var 2
# min_=1_000_000
# index_min=0
# for i in range(len(lines)):
#     if lines[i].count('G')<min_:
#         min_=lines[i].coune('G')
#         index_min=i
# line_min_G = lines[i]

# #считаю количество каждой буквы в строке
# letters = []
# nums = []
# for i in range(len(line_min_G)):
#     if line_min_G[i] in letters:
#         continue
#     else:
#         letters.append(line_min_G[i])
#         nums.append(line_min_G.count(line_min_G[i]))
#
# #вывожу на экран букву, которая встерчается чаще всего
# print(letters[nums.index(max(nums))])


#Task 6
"""
Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт. Строки содержат только заглавные буквы латинского алфавита (ABC…Z).
В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное расстояние между одинаковыми буквами в одной строке.
Answer: 1004
"""

# Довольно изящное решение с использованием строковой константы (можно ее создать вручную)

# import string
#
# max_distance = 0
# with open('24_Решу_ЕГЭ_Ч2_3.txt') as File:
#     for line in File:
#         if line.count('A')<25:
#             for i in string.ascii_uppercase:
#                     max_distance = max(max_distance,line.rfind(i)-line.find(i)) #rfind - поиск с конца
# print(max_distance)

# решение без строковой константы и строки букв

# max_distance = 0
# with open('24_Решу_ЕГЭ_Ч2_3.txt') as File:
#     for line in File:
#         if line.count('A')<25:
#             letters= [] #для оптимизации.
#             for i in range(len(line)-1):
#                 if line[i] in letters:
#                     continue
#                 else:
#                     letters.append(line[i])
#                 max_distance = max(max_distance,line.rfind(line[i])-i) #rfind - поиск с конца
# print(max_distance)

# то же,но без оптимизации, ведь такой вопрос не стоит

# max_distance = 0
# with open('24_Решу_ЕГЭ_Ч2_3.txt') as File:
#     for line in File:
#         if line.count('A')<25:
#             for i in range(len(line)-1):
#                 max_distance = max(max_distance,line.rfind(line[i])-i) #rfind - поиск с конца
# print(max_distance)