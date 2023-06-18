from itertools import *

MAX_W = 14
ar_variable = []

items_dict ={
    'Спички': 0.01,
    'Нож': 0.25,
    'Топор': 2,
    'Консервы': 2,
    'Одежда': 3,
    'Палатка': 8,
    'Компас': 0.1
}

for ar in permutations(items_dict):
    ar_variable.append(ar)

for a in ar_variable:
    print(*a)
