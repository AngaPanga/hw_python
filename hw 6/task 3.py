# Данное решение нашел в интернете, пытался разобраться с механикой 2 дня.
# По итогу почти полностью разобрался (не до конца понимаю как оно проверяет все диоганали)
# Но на основе лигики этого решения смог составить короткое решение задачи 2 "проверка пересечения ферзей"

class NQueens:
    def __init__(self, size):
        self.size = size
        self.count = 1
        self.solve()

    def solve(self):
        positions = [-1] * self.size
        self.put_queen(positions, 0)

    def put_queen(self, positions, target_row):
        if target_row == self.size:
            print(self.count)
            self.count += 1
            self.show_full_board(positions)
        else:
            for column in range(self.size):
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    self.put_queen(positions, target_row + 1)


    def check_place(self, positions, ocuppied_rows, column):
        for i in range(ocuppied_rows):
            if positions[i] == column or \
                positions[i] - i == column - ocuppied_rows or \
                positions[i] + i == column + ocuppied_rows:
                return False
        return True

    def show_full_board(self, positions):
        for row in range(self.size):
            line = ""
            for column in range(self.size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")

    def show_short_board(self, positions):
        line = ""
        for i in range(self.size):
            line += str(positions[i]) + " "
        print(line)

def main():
    NQueens(8)

main()