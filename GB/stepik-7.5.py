# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit)
    num //= 10
# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.
num = int(input())
while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    num //= 10
# Дано натуральное число n, \, (n \ge 10)n,(n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры.    
num = int(input())
largest = 0
smallest = 9
while num != 0:
    n = num % 10
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n
    num //= 10
print('Максимальная цифра равна', largest)
print('Минимальная цифра равна', smallest)

#Дано натуральное число. Напишите программу, которая вычисляет:
# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.

num = int(input())
sum_digits = 0
count_digits = 0
multiply_digits = 1
average_digits = 0
first_digit = 0
sum_first_last =0
last_digit = num % 10
another_num = num
while num != 0:
    digit = num % 10
    sum_digits += digit
    count_digits += 1
    multiply_digits *= digit
    num //= 10
first_digit = another_num // (10 ** (count_digits - 1))
average_digits = sum_digits / count_digits
sum_first_last = last_digit + first_digit
print(sum_digits, count_digits, multiply_digits, average_digits, first_digit, sum_first_last, sep = '\n')

# Дано натуральное число Напишите программу, которая определяет его вторую (с начала) цифру.
num = int(input())
another_num = num
count = 0
while num != 0:
    digit = num % 10
    count += 1
    num //= 10
second_digit = (another_num // 10 ** (count - 2)) % 10
print(second_digit)
# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
num = int(input())
last_digit = num % 10
uniq_digit = 0
while num != 0:
    next_digit = num % 10
    if next_digit != last_digit:
        uniq_digit += 1
    num //= 10
if uniq_digit == 0:
    print('YES')
else:
    print('NO')
# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при просмотре справа налево упорядоченной по неубыванию.
num = int(input())
flag = 'YES'
a = num % 10
while num:
    if a > num % 10:
        flag = 'NO'
    else:
        a = num % 10
    num //= 10
print(flag)
