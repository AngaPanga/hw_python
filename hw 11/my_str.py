import time

class My_str(str):
    """Новый класс строки с автором и временем"""

    def __new__(cls, val, name):
        """Наследование от класса str"""
        inst = super().__new__(cls, val)
        inst.name = name
        inst.time = time.time()
        return inst


if __name__ == '__main__':
    s1 = My_str('fff', 'a1')
    print(s1)
    print(s1.upper())
    print(s1.name)
    print(s1.time)
    print(s1)
    help(My_str)