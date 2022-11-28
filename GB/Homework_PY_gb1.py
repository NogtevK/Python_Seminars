# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Дополнительно: можете проверить, что это действительно число, и что это действительно входит в нужный диапазон

number_of_day = input('Введите день недели от 1 до 7. Вдруг выходной')

if number_of_day.isdigit():
    num = int(number_of_day)
    if num > 7 or num<1:
        print('это не цифра, обозначающая день недели')
    elif num > 5:
        print('Да! Выходной.')
    else:
        print('Нет! Рабочий.')
else:
    print('это не цифра')
        
# 2- Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Нужно написать таблицу истинности.        

for x in range(2):
    for y in range(2):
        for z in range(2):
            if not(x or z) == (not x and not y and not z):
                print(f'{x}\t{y}\t{z}\t{not(x or y or z) == (not x and not y and not z)}')

# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x_number = int(input('Введите координату Х:\n'))
y_number = int(input('Введите координату Y:\n'))

if x_number > 0 and y_number > 0:
    print('1-ая четверть')
elif x_number < 0 and y_number > 0:
    print('2-ая четверть')
elif x_number < 0 and y_number < 0:
    print('3-я четверть')
elif x_number > 0 and y_number < 0:
    print('4-ая четверть')
elif x_number == 0 and y_number ==0:
    print('точка начала координат')
elif x_number == 0:
    print('точка находится на оси X')
elif y_number == 0:
    print('точка находится на оси Y')

# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# Пример:
# - quarter = 1 = x∈(0, ∞) u y∈(0,∞)

number_of_quarter = int(input('Введите номер четверти:\n'))
if number_of_quarter not in range(1,5):
    print('Вы ввели неверное число')
elif number_of_quarter == 1:
    print('x∈(0, ∞) u y∈(0,∞)')
elif number_of_quarter == 2:
    print('x∈(0,-∞) u y∈(0,∞)')
elif number_of_quarter == 3:
    print('x∈(0,-∞) u y∈(0,-∞)')
else:
    print('x∈(0,∞) u y∈(0,-∞)')

# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5.09
# - A (7,-5); B (1,-1) -> 7.21


print('Введите, через пробел координаты 1-ой точки: ')
x_number1, y_number1 = map(int,input().split(' '))
print('Введите, через пробел координаты 2-ой точки: ')
x_number2, y_number2 = map(int,input().split(' '))

distance = float(((x_number2 - x_number1)**2 + (y_number2 - y_number1)**2) ** 0.5)
print(int(distance * 100)/100)



# def give_int(input_string):
#     while True:
#         try:
#             num = int(input(input_string))
#             return num
#         except:
#             print('Попробуйте еще раз. Вы ввели не число')
