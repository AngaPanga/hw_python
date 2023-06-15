STEP = 1
user_str = input('Введи строку: ')
str_dict = {}
str_dict_2 = {}

for el in user_str:
    if el in str_dict:
        str_dict[el] += STEP
    else:
        str_dict[el] = STEP

for key, el in str_dict.items():
    print(key, '-', el, 'повторений(-е, -я)')

print('-----------------------')

for el in user_str:
    if el not in str_dict_2:
        str_dict_2[el] = user_str.count(el)

for key, el in str_dict_2.items():
    print(key, '-', el, 'повторений(-е, -я)')

# Буквы повторяются из-за разных регистров