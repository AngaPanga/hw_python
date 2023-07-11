# Класс животные
class Animals:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


# Класс Птицы
class Birds(Animals):
    spec_dict = {
        '1':'Летает',
        '2':'Не летает'
    }
    def __init__(self, name, spec_op):
        self.__spec = self.spec_dict[spec_op]
        super().__init__(name)

    def print_to_str(self):
        return f'Класс {self.get_name()}\n{self.__spec}'


# Класс Рыбы
class Fishes(Animals):
    spec_dict = {
        '1':'Пресноводная',
        '2':'Морская'
    }
    def __init__(self, name, spec_op):
        self.__spec = self.spec_dict[spec_op]
        super().__init__(name)

    def print_to_str(self):
        return f'Класс {self.get_name()}\n{self.__spec}'


# Класс Человек
class Human(Animals):
    spec_dict = {
        '1':'Курит',
        '2':'Не курит'
    }
    def __init__(self, name, spec_op):
        self.__spec = self.spec_dict[spec_op]
        super().__init__(name)


    def print_to_str(self):
        return f'Класс {self.get_name()}\n{self.__spec}'


if __name__ == '__main__':
    h = Human('Человек', '1')
    print(h.print_to_str())
    f = Fishes('Рыба', '2')
    print(f.print_to_str())
    b = Birds('Птица', '2')
    print(b.print_to_str())