class Arch:
    '''Класс архив, содержит два списка'''
    num_list = []
    str_list = []

    def __init__(self, n, s):
        '''Присвоение переменным класса значения и добавление в списки'''
        self.num = n
        self.string = s
        self.num_list.append(n)
        self.str_list.append(s)

    def __str__(self):
        return f'Экземпляр класса. ' \
               f'Содержит: значение {self.num} и строку {self.string}'

    def __repr__(self):
        return f'Arch({self.num}, {self.string})'


if __name__ == '__main__':
    arch_1 = Arch(5, 'fff')
    print(arch_1.num_list, arch_1.str_list)
    arch_2 = Arch(7, 'aaa')
    print(arch_2.num_list, arch_2.str_list)
    print(arch_1)
    print(repr(arch_2))
    help(Arch)