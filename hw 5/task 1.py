# Функция разделения Папка Имя Расширение

def file_stat(file_str):
    box = file_str.split('/')
    box_2 = box.pop(-1)
    path_file = '/'.join(box)
    name_file, type_file = box_2.split('.')
    return path_file, name_file, type_file

print(file_stat('C:/hh/ss/kk/zz/aa.txt'))