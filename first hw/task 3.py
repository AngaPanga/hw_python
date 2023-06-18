# Программа проверки числа на принадлежность множеству простых чисел

n = int(input('Введите число: '))
easy_number = True

for i in range(2, int((n**0.5)//1 + 1)):
    if n % i == 0:
        easy_number = False

if easy_number:
    print('Число является простым!')
else:
    print('Число не является простым!')