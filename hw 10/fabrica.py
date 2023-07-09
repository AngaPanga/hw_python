import animals_classes

class fabr_animals():
    def __init__(self, tp_animal, name, spc):
        self.new_animal = tp_animal(name,spc)

    def result(self):
        return self.new_animal.print_to_str()


if __name__ == '__main__':
    ani = fabr_animals(animals_classes.Human, 'Чел', '2')
    print(ani.result())