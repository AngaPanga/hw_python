# Пересечение ферзей
# 1,8 2,4 3,1 4,3 5,6 6,2 7,7 8,5
# 1,1 2,3 3,5 4,7 5,2 6,4 7,6 8,8

CONST = 1

# Функция преоброзования строки в двумерный словарь
def convert_positions(user_str):
    lst_start = user_str.split()
    lst_finish = []
    for el in lst_start:
        lst_finish.append(list(map(int, el.split(','))))
    return lst_finish

# Функция проверки пересечения ферзей
def check_posititions(lst_p):
    # конвертируем наборы значений в 2 списка столбцы и строки
    clms, rows = map(list, zip(*lst_p))
    # проверяем дубликаты по столбцам
    for el in clms:
        if clms.count(el) > CONST:
            return False
    # проверяем дубликаты по строкам
    for el in rows:
        if rows.count(el) > CONST:
            return False
    # при отсутствии дубликатов строк и столбцов, конвертируем два словаря в один
    # где индекс это столбец, а строка значение
    result_list = []
    for i in range(len(clms)):
        result_list.insert(clms[i]-CONST, rows[i]-CONST)
    # Проверяем диагонали, идея в последовательном прибавлении и отнятии 1 от взятой кординаты
    # Если есть совпадения при смещении значит на одной диагонали
    for i in range(len(result_list)-CONST):
        for j in range(CONST, len(result_list) - i):
            if result_list[i] + j == result_list[i + j] or result_list[i] - j == result_list[i + j]:
                return False
    return True

if __name__ == '__main__':
    lst_pos = convert_positions(input('Введите кординаты ферзей вида "1,1 2,2 ... 8,8": '))
    if check_posititions(lst_pos):
        print('Ферзи не пересекаются.')
    else:
        print('Ферзи пересекаются.')
