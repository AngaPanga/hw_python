import csv, random, json


F_NAME = 'ABCcof-ts.csv'
MIN = -30
MAX = 30
NULL = 0


def write_file(data):
    with open(F_NAME, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def gen_cof ():
    count = int(input("Введите количество строк коэфицентов: "))
    for _ in range(count):
        cof_list = [random.randrange(MIN, MAX),
                    random.randrange(MIN, MAX),
                    random.randrange(MIN, MAX)]
        write_file(cof_list)


def write_json(func):
    def wrapper():
        with open('ans.json', 'w') as file:
            json.dump(func(), file)
    return wrapper


@write_json
def arefmetic():
    data = []
    with open(F_NAME, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    res_data = []
    for nums in data:
        a, b, c = map(int, nums)
        d = -1*(b**2)+4*a*c
        if d < NULL:
            res_data.append(f'Для коэфицентов a = {a}, b = {b}, c = {c}, решений нет.')
        elif d == NULL:
            x = b / (2 * a)
            res_data.append(f'Для коэфицентов a = {a}, b = {b}, c = {c}, есть один корень уровнения. x = {x}')
        else:
            x1 = (b - d ** 0.5) / (2 * a)
            x2 = (b + d ** 0.5) / (2 * a)
            res_data.append(f'Для коэфицентов a = {a}, b = {b}, c = {c},'
                            f' есть два кореня уровнения. x1 = {x1} и x2 = {x2}')
    return res_data


if __name__ == '__main__':
    gen_cof()
    arefmetic()