class Regtangle:
    '''Класс прямоугольник'''
    COF_0 = 0
    COF_1 = 1
    COF_2 = 2

    def __init__(self, *args):
        ''' Конструктор'''
        if len(args) > self.COF_1:
            self.a, self.b, *_ = args
        else:
            self.a, *_ = args
            self.b = self.a

    def __add__(self, other):
        ''' сложение периметров '''
        prm = self.perimetr() + other.perimetr()
        return Regtangle(prm // self.COF_2 / self.COF_2)

    def __sub__(self, other):
        ''' вычетание периметров '''
        prm = self.perimetr() - other.perimetr()
        return Regtangle(abs(prm // self.COF_2 / self.COF_2))

    def perimetr(self):
        return self.COF_2 * (self.a + self.b)

    def place(self):
        return self.a * self.b

    def __eq__(self, other):
        return self.place() == other.place()

    def __ne__(self, other):
        return self.place() != other.place()

    def __lt__(self, other):
        return self.place() < other.place()

    def __le__(self, other):
        return self.place() <= other.place()

    def __gt__(self, other):
        return self.place() > other.place()

    def __ge__(self, other):
        return self.place() >= other.place()

    def __str__(self):
        return f'Класс прямоугольник со сторонами a, b = {self.a}, {self.b}'

    def __repr__(self):
        return f'Regtangle({self.a}, {self.b})'

if __name__== '__main__':
    print('Первый прямоугольник')
    quad = Regtangle(6, 7)
    print('периметр = ', quad.perimetr())
    print('площадь = ', quad.place())
    print('Второй прямоугольник')
    quad_2 = Regtangle(4)
    print('периметр = ', quad_2.perimetr())
    print('площадь = ', quad_2.place())
    print('+++++++++')
    quad_3 = quad + quad_2
    print('периметр = ', quad_3.perimetr())
    print('площадь = ', quad_3.place())
    print('-----------')
    quad_4 = quad - quad_2
    print('периметр = ', quad_4.perimetr())
    print('площадь = ', quad_4.place())
    print('=====================')
    print(quad == quad_2)
    print(quad != quad_2)
    print(quad < quad_2)
    print(quad <= quad_2)
    print(quad > quad_2)
    print(quad >= quad_2)
    print('~~~~~~~~~~~~~~~')
    print(quad)
    print(repr(quad))
    print(quad_2)
    print(repr(quad_2))
