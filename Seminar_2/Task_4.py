# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
# Пояснение:
# Ввожу N = 5
# И мне нужно получить список из пяти элементов, причем сами элементы могут быть от -5 до 5,
# после этого пользователь через пробел вводит индексы элементов, которые нужно перемножить между собой,
# перемножаем элементы и получаем результат.


from itertools import product
import random
 
list = []
n = int(input('Введите число элементов: '))
for i in range(n):
    list.append(random.randint(-n, n))

print(f'Cписок из {n} элементов = ', list)


number_elements = input('Введите индекс: ').split()
number_position = 0
priduct_number = 1
for i in range(len(number_elements)):
    number_position = int(number_elements[i])
    priduct_number *= list[i]

print('Произведение индексов =', priduct_number)









