# # 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
  
# #    *Примеры:* 
  
# #    - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

number=abs(int(input('Введите число:\n')))
r=range(-number,number+1)
arr=list(r)
print(arr)


# # 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
  
# #    *Примеры:*
   
# #    - 6,78 -> 7
# #    - 5 -> нет
# #    - 0,34 -> 3

number=float(input('Введите число:\n'))
print(int(number*10)%10)


# #3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%.
# #- 6.78 -> 7
# #- 5 -> no
# #- 0.34 -> 3
# #max_num = 100

import random

numbers = []
for i in range(10):
    numbers.append(random.randint(0,100))
print(numbers)
count = 0
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
for i in numbers:
    if i < (maximum * 0.1): 
        count +=1
print(maximum)        
print(count)



