import math

num1 = math.sqrt(2)     # вычисление корня квадратного из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)
#На плоскости евклидово расстояние между двумя точками
import math

x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())
p = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2) 
print(p)
#Напишите программу определяющую площадь круга и длину окружности по заданному радиусу RR.
from math import pi

r = float(input())
s = pi * r ** 2
c = 2 * pi * r
print(s)
print(c)
#Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
import math

a, b = float(input()), float(input())
print((a + b) / 2)
print(math.sqrt(a * b))
print((2 * a * b) / (a + b))
print(math.sqrt((((a ** 2) + (b ** 2)) / 2)))
#Напишите программу, вычисляющую значение тригонометрического выражения
from math import *

x = radians(float(input()))
val = sin(x) + cos(x) + pow(tan(x), 2)
print(val)
#Напишите программу, вычисляющую значение ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.
from math import *

x = float(input())
print(ceil(x) + floor(x))
#Даны три вещественных числа aa, bb, cc. Напишите программу, которая находит вещественные корни квадратного уравнения 
from math import *

a, b, c = float(input()), float(input()), float(input())
d = pow(b, 2) - (4 * a * c)
if d < 0:
    print('Нет корней')
elif d == 0:
    x = (- b) / (2 * a)
    print(x)
elif d > 0:
    x1 = (- b + sqrt(d)) / (2 * a)
    x2 = (- b - sqrt(d)) / (2 * a)
    maxx = max(x1, x2)
    minx = min(x1, x2)
    print(minx)
    print(maxx)
#Правильный многоугольник — выпуклый многоугольник, у которого равны все стороны и все углы между смежными сторонами. Площадь правильного многоугольника с длиной стороны aa и количеством сторон nn
from math import *

n, a = int(input()), float(input())
s = (n * pow(a, 2)) / (4 * tan(pi / n))
print(s)

