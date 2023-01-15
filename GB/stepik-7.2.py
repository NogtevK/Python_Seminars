# Даны два целых числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно.
m, n = int(input()), int(input())
for i in range(m, n+1):
    print(i)
# Даны два целых числа mm и nn. Напишите программу, которая выводит все числа от mm до nn включительно в порядке возрастания, если m < nm<n, или в порядке убывания в противном случае.
m, n = int(input()), int(input())
if m < n:
    for i in range(m, n + 1, 1):
        print(i)
else:
    for i in range(m, n - 1, -1):
        print(i)
# Даны два целых числа mm и nn (m > nm>n). Напишите программу, которая выводит все нечетные числа от mm до nn включительно в порядке убывания.
m, n = int(input()), int(input())
if m % 2 == 0:
    for i in range(m - 1, n - 1, -2):
        print(i)
else:
    for i in range(m, n - 1, -2):
        print(i)
# Даны два натуральных числа mm и nn ( m \le nm≤n). Напишите программу, которая выводит все числа от mm до nn включительно удовлетворяющие хотя бы одному из условий:
m, n = int(input()), int(input())
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)
# Дано натуральное число nn. Напишите программу, которая выводит таблицу умножения на nn.
n = int(input())
for i in range(1, 11):
    multiply = n * i
    print(n, 'x', i, '=', multiply)        