# Добавление исключения
# Угадай число
from random import randint


class ExInt(Exception):
    def __str__(self):
        return 'Ошибка! Введенные данные не являются целым числом.'


MAX_COUNT = 10

print('Число загадано! У тебя 10 попыток его угадать.')
rnd_num = randint(1, 1001)
count = 0
while count < MAX_COUNT:
    print('    Попыток осталось:', MAX_COUNT-count)
    box = input('Введи свой варинт числа: ')
    if box.isdigit():
        user_num = int(box)
    else:
        raise ExInt()
    match user_num:
        case user_num if user_num == rnd_num:
            count += 1
            print('Число угадано! Количество попыток использовано: ', count)
            break
        case user_num if user_num > rnd_num:
            count += 1
            print('Загаданое число меньше.')
        case user_num if user_num < rnd_num:
            count += 1
            print('Загаданое число больше.')
else:
    print('Все попытки использованы! Вы проиграли!')
