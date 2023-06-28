import os

ZERO = 0
STEP = 1

def renames_files(folder = '', ch_ext = '.txt', start_count = STEP):
    os.chdir(folder)
    list_files = os.listdir()
    ch_lst_files = []
    for file in list_files:
        old_name, ext_file = os.path.splitext(file)
        if ext_file == ch_ext:
            ch_lst_files.append(file)
    l_num = len_num(len(list_files))
    for file in ch_lst_files:
        old_name, ext_file = os.path.splitext(file)
        new_name = old_name + '-' + str(start_count).rjust(l_num, '0') + ext_file
        os.rename(file, new_name)
        start_count += STEP

def len_num(num):
    count = ZERO
    while num > ZERO:
        count+= STEP
        num //= 10
    return count

if __name__ == '__main__':
    renames_files('222')
