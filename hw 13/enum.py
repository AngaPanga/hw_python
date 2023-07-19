# Программа проверки числа на принадлежность множеству простых чисел

class ExEnum(Exception):
    def __str__(self):
        return 'Ошибка! Число не является простым.'


n = int(input('Введите число: '))
easy_number = True

for i in range(2, int((n**0.5)//1 + 1)):
    if n % i != 0:
        easy_number = True
    else:
        raise ExEnum()

if easy_number:
    print('Число является простым!')
