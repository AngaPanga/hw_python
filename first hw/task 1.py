# Являетсля ли год высокосным.

COF1 = 4
COF2 = 400
COF3 = 100

get_year = int(input('Введите год для проверки: '))
if get_year < COF2 and get_year % COF1 == 0:
    print('Год высокосный!')
elif get_year % COF2 == 0 or (not get_year % COF3 == 0) and get_year % COF1 == 0:
    print('Год высокосный!')
else:
    print('Год не высокосный!')
