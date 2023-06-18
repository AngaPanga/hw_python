count_users = int(input('Введите количество друзей: '))
users_dict = {}
items_lst = []
items_set = set()

for _ in range(count_users):
    name = input('Введите имя друга: ')
    users_dict[name] = set(input('Введите список вещей через пробел: ').lower().split())
    items_set &= users_dict[name]

for key in users_dict:
    items_lst.extend(list(users_dict[key]))


print('Общий список всех предметов.\n', *(set(items_set)))
print(items_set)

