# Строка для примера
# это механизм позволяющий получить случайное слово или список слов по заданным параметрам пользователя

def space_count(val, len_s):
    return (len_s - len(val)) * ' '

STEP = 1
count = 1
len_str = 0
INDENT = 10

user_str = input('Введите строку: ')
ar = user_str.split()
ar.sort()

for el in ar:
    x = len(el)
    if len_str < x: len_str = x

for el in ar:
    if count < INDENT: print(end=' ')
    print(str(count) + '. ' + space_count(el, len_str) + el)
    count += STEP
