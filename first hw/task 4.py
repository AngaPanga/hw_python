# Угадай число
from random import randint
MAX_COUNT = 10

print('Число загадано! У тебя 10 попыток его угадать.')
rnd_num = randint(1, 1001)
count = 0
while count < MAX_COUNT:
    print('    Попыток осталось:', MAX_COUNT-count)
    user_num = int(input('Введи свой варинт числа: '))
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
