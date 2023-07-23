import My_Ex as MyEx
import User_cls as Usr
import csv


class Project:
    def __init__(self, users):
        self.users = users
        self.admin = None

    @classmethod
    def load(cls, filename):
        try:
            users = []
            with open(filename, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                for row in reader:
                    users.append(Usr.User(*row))
        except Exception as e:
            print(f'При открытии файла {filename} возникла ошибка {e}. ')
        else:
            return Project(users)

    def __str__(self):
        return 'Проект создан'

    def login(self, name, user_id):
        user_new = Usr.User(name, user_id)
        if user_new not in self.users:
            raise MyEx.AccessExp
        for user in self.users:
            if user_new == user:
                self.admin = user

    def add_user(self, name, user_id, level):
        if int(self.admin.level) >= int(level):
            raise MyEx.LevelExp
        self.users.append(Usr.User(name, user_id, level))


if __name__ == '__main__':
    prj = Project.load('users.csv')
    #prj.login('Саша', '115')
    prj.login('Анна', '101')
    #prj.add_user('Саша', '115', '1')
    prj.add_user('Саша', '115', '7')
    for u in prj.users:
        print(u)