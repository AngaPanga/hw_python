# Вывод пикл строки
import csv, pickle

def pic_in_csv(f_name):
    with open(f_name, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(pickle.dumps(row))

if __name__ == '__main__':
    pic_in_csv('new_csv.csv')