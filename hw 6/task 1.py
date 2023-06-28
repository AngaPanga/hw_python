# Проверка даты с доступностью из терминала
from sys import *

MIN = 1
DAY_LINIT = 31
MONTH_LIMIT = 12
MAX_YEAR = 2000
MIN_YEAR = 1000
SHORT_M = (4, 6, 9, 11)
FEB_M = 2
FEB_D = 29

def is_date(day = 0, month = 0, year = 0):
    if day < MIN or month < MIN:
        return False
    if day > DAY_LINIT or month > MONTH_LIMIT or MAX_YEAR < year or year < MIN_YEAR:
        return False
    if month in SHORT_M and day == DAY_LINIT:
        return False
    if month == FEB_M and day > FEB_D:
        return False
    if month == FEB_M and day == FEB_D and check_year(year):
        return False
    return True

def check_year(y):
    cof_1 = 4
    cof_2 = 100
    cof_3 = 400
    res = 0
    if y % cof_1 == res and y % cof_2 != res or y % 400 == res:
        return False
    return True

if __name__ == '__main__':
    _, *params = argv
    if is_date(*map(int, params)):
        print('Дата корректна.')
    else:
        print('Такой даты нет!')