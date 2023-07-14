class Matrix:
    STEP = 1
    NL = '\n'
    def __init__(self, colums, rows):
        self.__clms = colums
        self.__rws = rows
        self.matrix = []

    def get_clms(self):
        return self.__clms

    def get_rws(self):
        return self.__rws

    def input_matrix(self):
        for row in range(self.__rws):
            print(f'Заполнение строки {row + self.STEP}')
            temp_list = []
            for el in range(self.__clms):
                temp_list.append(int(input(f'Введите элемент для столбца {el + self.STEP}: ')))
            self.matrix.append(temp_list)

    def __str__(self):
        string_mtx = ''
        for row in self.matrix:
            for el in row:
                string_mtx += str(el) + ' '
            string_mtx += self.NL
        return string_mtx

    def __add__(self, other):
        if self.get_clms() == other.get_clms() and self.get_rws() == other.get_rws():
            tmp_mtx = Matrix(self.get_clms(),self.get_rws())
            for row in range(self.get_rws()):
                tmp_lst = []
                for el in range(self.get_clms()):
                    tmp_lst.append(self.matrix[row][el] + other.matrix[row][el])
                tmp_mtx.matrix.append(tmp_lst)
            return tmp_mtx
        else:
            print('Ошибка! Размеры матриц не совпадают -> сложение не возможно!')
            return None

    def __eq__(self, other):
        if self.get_clms() == other.get_clms() and self.get_rws() == other.get_rws():
            if self.matrix == other.matrix:
                return True
        return False


if __name__ == '__main__':
    m_1 = Matrix(2, 2)
    m_1.input_matrix()
    print(m_1)
    m_2 = Matrix(2, 2)
    m_2.input_matrix()
    print(m_2)
    print('---- Сумма матриц ----')
    m_3 = m_1 + m_2
    print(m_3, end='')
    print()
    print(m_1 == m_2)