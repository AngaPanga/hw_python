MAX_POINTS = 2

def gen_file(name_file):
    if '.' in name_file and list(name_file).count('.') < MAX_POINTS:
        with open(name_file, 'w', encoding='utf-8') as file:
            file.close()
    else:
        print('Имя файла ошибочно.')

if __name__ == '__main__':
    gen_file("test.txt")