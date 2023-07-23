import csv, random


class Check_f_name:
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value.isalpha():
            if value.islower():
                raise Exception('Ошибка! Ф.И.О состоит только из букв нижнего регистра.')
            raise Exception('Ошибка! Ф.И.О содержат цифры.')
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name

# -------------------------------------------------------

class Student:
    full_name = Check_f_name()

    def __init__(self, full_name, file_name):
        self.full_name = full_name
        self.subjects = self.__lst_subjects(file_name)
        self.data_tests = self.__create_data_tests()
        self.data_grade = self.__create_data_grades()

    def __lst_subjects(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            tmp = list(reader)
            return tmp[0]

    def __create_data_tests(self):
        data_dict = {}
        for sbj in self.subjects:
            data_dict[sbj] = list(random.randint(1, 100) for _ in range(5))
        return data_dict

    def __create_data_grades(self):
        grade_dict = {}
        for key, val in self.average_tests().items():
            if 80 < val < 101:
                grade_dict[key] = 5
            elif 60 < val < 81:
                grade_dict[key] = 4
            elif 40 < val < 61:
                grade_dict[key] = 3
            elif 20 < val < 41:
                grade_dict[key] = 2
            else:
                print('Слишком низкие результаты по предмету ', key)
        return grade_dict

    def average_tests(self):
        avrg_t = {}
        for key, val in self.data_tests.items():
            avrg_t[key] = sum(val)/len(val)
        return avrg_t

    def average_grade(self):
        return sum(el for el in self.data_grade.values())/len(self.data_grade)


if __name__ == '__main__':
    s = Student('Петров Петр Петрович', 'sbjs.csv')
    for key, el in s.average_tests().items():
        print(key, ' - ', el)
    print('Средняя оценка по предметам: ', s.average_grade())