# Задача 5
import os
import random
import generator_files as gf
import generate_name as gn

MIN = 1

def check_path(folder = "new_dir"):
    while True:
        if not os.path.exists(folder) and folder != '':
            os.mkdir(folder)
            break
        elif folder == '':
            print("Ошибка! Имя папки не может быть пустым")
            folder = input('Введите имя папки: ')
        else:
            break
    return folder

def generates(max_count = 1, ext_list = ['.txt'], in_folder = 'nd'):
    in_folder = check_path(in_folder)
    list_files = []
    if len(ext_list) == MIN:
        for _ in range(max_count):
            list_files.append(os.path.join(in_folder, gn.gen_name() + ext_list[0]))
    else:
        for el in ext_list:
            box = random.randint(MIN, max_count//2)
            for _ in range(box):
                list_files.append(os.path.join(in_folder, gn.gen_name() + el))
            max_count -= box
    for el in list_files:
        gf.gen_file(el)

if __name__ == '__main__':
    #generates(5)
    generates(10, ['.txt', '.png',], '')