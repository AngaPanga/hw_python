import pickle, csv

def pic_read(file_name):
    with open(file_name, 'rb') as file:
        return pickle.load(file)

def csv_write(file_csv, data):
    heads = data[0].keys()
    with open(file_csv, 'a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=heads)
        writer.writeheader()
        writer.writerows(data)
    print('save complete')

if __name__ == '__main__':
    dt = [
        {11: (1, 1, 1, 1), 22: (2, 2, 2, 2)},
        {11: ('a', 'a', 'a', 'a'), 22: ('b', 'b', 'b', 'b')},
        {11: (1.0, 1.0, 1.0, 1.0), 22: (2.0, 2.0, 2.0, 2.0)}
    ]
    dt_f = 'data.pickle'
    with open(dt_f, 'wb') as f:
        pickle.dump(dt, f)

    res = pic_read(dt_f)
    csv_write('new_csv.csv', res)
