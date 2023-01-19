# что выведет код
for i in range(10):
    print(i, end='*')
    if i > 6:
        break
# что выведет код
n = 10
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n, end='*')

mult = 1
for i in range(1, 11):
   if i % 2 == 0:
      continue
   if i % 9 == 0:
      break
   mult *= i
print(mult)

# На вход программе подается число n>1. Напишите программу, которая выводит его наименьший отличный от 1 делитель
num = int(input())
for i in range(2, num + 1):
    if num % i == 0:
        break
print(i)

#На вход программе подается натуральное число Напишите программу, которая выводит числа от 1 до n включительно за исключением:
# чисел от 5 до 9 включительно;
# чисел от 17 до 37 включительно;
# чисел от 78 до 87 включительно.
num = int(input())
for i in range (1, num + 1):
    if 9 >= i >= 5:
        continue
    if 37 >= i >= 17:
        continue    
    if 87 >= i >= 78:
        continue
    print(i) 