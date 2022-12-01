# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.
 
list_1 = list(map(int, input("Введите целые числа, используя пробел как разделитель:\n").split()))

max = list_1[0]
min = list_1[0]
for i in range(len(list_1)):
    if list_1[i] > max:
        max = list_1[i] 
    elif list_1[i] < min:
            min = list_1[i]
print(f'Max number: {max}')
print(f'Min number: {min}')  
 
            

# 2. Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.
def nok(a, b):
    if a > b:
        largest = a
    else:
        largest = b
    while True:
        if largest % a == largest % b == 0:
            nok_res = largest
            break
        largest += 1
    return nok_res


a, b = int(input('Type value for first number: ')), \
       int(input('Type value for second number: '))
print(nok(a, b))
