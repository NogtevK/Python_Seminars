total = 0
for i in range(1, 6):
    total += i
    print(total, end='')
# На вход программе подаются два целых числа aa и bb (a \le b)(a≤b). Напишите программу, которая подсчитывает количество чисел в диапазоне от aa до bb включительно, куб которых оканчивается на 44 или 99.
a, b = int(input()), int(input())
counter = 0

for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        counter += 1
print(counter)
# На вход программе подается натуральное число nn, а затем nn целых чисел, каждое на отдельной строке. Напишите программу, которая подсчитывает сумму введенных чисел.
n = int(input())
sum = 0
for i in range(n):
    n = int(input())
    sum += n
print(sum)
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет значение выражения
from math import *

n = int(input())
num = 0
for i in range(1, n+1):
    num += 1 / i
print(num - log(n))

# На вход программе подается натуральное число nn. Напишите программу, которая подсчитывает сумму тех чисел от 11 до nn (включительно) квадрат которых оканчивается на 2, \, 52,5 или 88.
from math import *

n = int(input())
sum = 0
counter = 0
for i in range(1, n + 1):
    if pow(i, 2) % 10 == 2 or pow(i, 2) % 10 == 5 or pow(i, 2) % 10 == 8:
        sum += i
        counter += 1
if counter == 0:
    print(counter)
else:    
    print(sum)
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет n!    
from math import *

n = int(input())
print(factorial(n))
# Напишите программу, которая считывает 10 чисел и выводит произведение отличных от нуля чисел.
multiply = 1
for i in range (1, 11):
    num = int(input())
    if num != 0:
        multiply *= num
print(multiply)
# На вход программе подается натуральное число nn. Напишите программу, которая вычисляет сумму всех его делителей.
n = int(input())
sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum += i
print(sum)
# На вход программе подается натуральное число nn. Напишите программу вычисления знакочередующей суммы 
n = int(input())
sum = 0
for i in range(0, n + 1):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
# На вход программе подается натуральное число nn, а затем nn различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
maxup = 1
maxdown = 0
for i in range(1, n + 1):
    num = int(input())
    if num > maxup:
        maxup, maxdown = num, maxup
    elif maxdown < num < maxup:
        maxdown = num
print(maxup)
print(maxdown)
# Напишите программу, которая считывает последовательность из 10 целых чисел и определяет является ли каждое из них четным или нет.
counter = 0
for i in range(1, 11):
    num = int(input())
    if num % 2 == 0:
        counter += 1
        
if counter == 10:
    print('YES')
else:
    print('NO')
# Напишите программу, которая считывает натуральное число nn и выводит первые nn чисел последовательности Фибоначчи.
n = int(input())
fib1 = 0
fib2 = 1
print(fib2, end=' ')
for i in range(n - 1):
    if n >= 2:
        fib2 = fib1 + fib2
        fib1 = fib2 - fib1
        print(fib2, end=' ')
