st = open("number_24/24_Решу_Егэ_Ч1.txt").readline()

f = 'X'
# запуск счетчика
i = 0
# возможный алфавит и его связь со значением счетчика
alp = {
    0 : "Y",
    1 : "Z",
    2 : "X"
}

# пока мы можем найти продолжение строки...
while f in st:
    # добавляем потенциальный фрагмент строки, его еще не нашли, но мы предполагаем
    # i%3 позволит всегда получить 0, 1 или 2
    f += alp[i%3]
    print(f)
    i +=1

print("--------------------------------")
print (len(f[:-1]))