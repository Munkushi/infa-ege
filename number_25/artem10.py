"""
Отработка 

Task 2

Назовём нетривиальным делителем натурального числа его делитель, не равный единице и самому числу. Например, 
у числа 6  есть два нетривиальных делителя: 2 и 3. Найдите все натуральные числа, принадлежащие отрезку  [289123456;389123456] 
и имеющие ровно три нетривиальных делителя. Для каждого найденного числа запишите в ответе его
наибольший нетривиальный делитель. Ответы расположите в порядке возрастания.

Например, в диапазоне [5;16] ровно три различных натуральных делителя имеет число 16, поэтому для этого диапазона  
вывод на экране должна содержать следующие значения:

16 8

Ответ:
294499921 2248091
352275361 2571353
373301041 2685619
"""

for i in range(289123456, 389123456 + 1):
    divisors = set()
    if int(i ** 0.5) ** 2 != i: continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j ==0:
            divisors.add(j)
            divisors.add(i // j)
            if len(divisors) > 3: break
    if len(divisors) == 3:
        print(i, i // min(divisors))
# не работает
# 294499921 2248091
# 352275361 2571353
# 373301041 2685619