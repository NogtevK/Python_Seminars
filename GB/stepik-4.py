#Напишите программу, которая выводит текст:
print('''"Python is a great language!", said Fred. "I don't ever remember having this much fun before."''')
#«Hello [введенное имя] [введенная фамилия]! You just delved into Python»
firstname = input()
lastname = input()
print('Hello ' + firstname + ' ' + lastname + '! ' + 'You just delved into Python')
#«Футбольная команда [введённая строка] имеет длину [длина введённой строки] символов».
fclub = input()
length = len(fclub)
strlength = str(length)
print('Футбольная команда ' + fclub + ' имеет длину ' + strlength + ' символов')
#Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
town1, town2, town3 = input(), input(), input()
l1 = len(town1)
l2 = len(town2)
l3 = len(town3)
maxl = max(l1, l2, l3)
minl = min (l1, l2, l3)
if minl == l1:
    print(town1)
elif minl == l2:
    print(town2)
elif minl == l3:
    print(town3)
if maxl == l1:
    print(town1)
elif maxl == l2:
    print(town2)
elif maxl == l3:
    print(town3)
#Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет можно ли из длин этих строк построить возрастающую арифметическую прогрессию.
#Программа должна вывести строку «YES», если из длин введенных слов можно построить арифметическую прогрессию, «NO» в ином случае.
a, b, c = len(input()), len(input()), len(input())
if (2 * b - c - a)*(2 * c - b - a)*(2 * a - b - c) == 0:
    print('YES')
else:
    print('NO')
#Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введенной строке есть подстрока «синий» и «NO» в противном случае.
s1, s2 = input(), 'синий'
if s2 in s1:
    print('YES')
else:
    print('NO')
#Напишите программу, которая считывает одну строку, после чего выводит «YES», если в введённой строке есть подстрока «суббота» или «воскресенье», и «NO» в противном случае.
s1, s2, s3 = input(), 'суббота', 'воскресенье'
if s2 in s1:
    print('YES')
elif s3 in s1:
    print('YES')
else:
    print('NO')
#Будем считать email адрес корректным, если в нем есть символ собачки (@) и точки. Напишите программу проверяющую корректность email адреса.
s1 = input()
if '@' in s1:
    if '.' in s1:
        print('YES')
    else:
        print('NO')
else:
    print('NO')   