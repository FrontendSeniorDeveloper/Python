# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11
 
num = input('Введите вещественное число: ')
print(f'Введённое число = {num}')

summ = 0
for i in num:
    if i != '.':
        summ += int(i)

print(f'Сумма цифр числа = {summ}')



