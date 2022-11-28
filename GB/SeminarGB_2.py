# print('vzuh')
# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов. 
#     *Пример:* 
#     - Для N = 5: 
# 1, -3, 9, -27, 81

n = int(input('Введите число: '))
for i in range(n):
    print((-3)**i, end=' ')


# 2. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.
text = list(input('Введите текст: '))
text2 = list(input('Введите текст 2: '))
print(text, text2)
num = 0
for i in range(len(text2)):
    for j in range(len(text)):
        if text[j]==text2[i]:
           num+=1
print(num)

# result = a.count(b)
a = list(input())
b = list(input())
cnt = 0
for i in range(len(a)-len(b)+1):
    if a[i] == b[0]:
        switch=True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                switch=False
                break
        if switch:
            cnt += 1
print(cnt)

# word = 'python'
# print(word[2:])
# print(word[:2])
# print(word[1:3])
