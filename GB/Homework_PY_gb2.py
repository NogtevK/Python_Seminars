# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

def get_int(float_):
    while round(float_, 9) % 10 !=0:
        float_ = round(float_,9) * 10
    new_int = int(float_)
    return new_int // 10

def sum_of_digits(number):
    sum = 0
    while number > 0:
        sum += (number %10)
        number = number // 10
    return sum
try:
    n = float(input('Введите вещественное число:\n'))
    num = abs(n)
    print(get_int(num))
    print(sum_of_digits(get_int(num)))
except ValueError:
    print('Вы ввели не число')

# Second solution

number = input('введите число:\n')
num_1 = number.replace('.', "").replace('-', "")
result = round(sum(int(i) for i in num_1))
print(result) 
    
# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

n = int(input('Введите число N:\n'))
set_multiply = []   # new list
previous_multiply = 1   # first number in list
for num in range(1, n + 1):
    set_multiply.append((previous_multiply) * num)
    previous_multiply = previous_multiply * num
print('N =', n, ', Factorial N: ', set_multiply )

# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

import random

num = int(input('Введите число N:\n')) # кол-во элементов в списке
count = 0
rand = [random.randint(-100, 100) for i in range(num)] # заполняем лист рандомными числами -100 до 100. 

for i in range(num):
    if rand[i] < 0:
        rand.insert(i + 1, count)
if rand[-1] < 0:
    rand.append(0)
print(rand)

# 4 - По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее человек, на котором остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. Процесс продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру. Если хотите делать паузы, то импортируйте библиотеку time и используйте оттуда функцию sleep. Определите номер этого человека и количество монет, которые оказались у него в конце игры.

# 4 - (если не получается, то альтернативная задача). Составьте алгоритм нахождения случайного числа без использования библиотеки random.