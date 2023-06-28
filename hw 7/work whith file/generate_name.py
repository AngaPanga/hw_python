from random import *

MIN = 3
MAX = 6

def names_list(count = MIN):
    list_names = []
    for _ in range(count):
        list_names.append(gen_name())
    return  list_names

def gen_name():
    uper_char_list = 'WRTPSDFGHJKLZXCVBNM'
    char_list = 'qwertyuiopasdfghjklzxcvbnm'
    return choice(uper_char_list) + ''.join(choices(char_list, k = randint(MIN, MAX)))

if __name__ == '__main__':
    print(names_list(5))