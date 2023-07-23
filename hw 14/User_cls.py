class User:
    def __init__(self, name, id, level = '7'):
        self.__name = name
        self.__id = id
        self.__lvl = level

    def __str__(self):
        return f'Пользователь: {self.__name}, id: {self.__id}, уровень доступа: {self.__lvl}'

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def level(self):
        return self.__lvl

    def __eq__(self, other):
        if self.__name == other.name and self.__id == other.id:
            return True
        return False


if __name__ == '__main__':
    p1 = User('Ivan', '135', '3')
    print(p1.name, p1.id, p1.level)
    p2 = User('Petr', '148', '1')
    p3 = User('Ivan', '77', '2')
    p4 = User('Ivan', '135', '4')
    print(p1 == p2)
    print(p1 == p2)
    print(p1 == p3)
    print(p1 == p4)