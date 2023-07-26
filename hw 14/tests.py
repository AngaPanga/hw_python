# В общем от изначального вида кода пришел к такому.
# Но тесты всеравно у меня в пайчарме не хотят работать.
# В конце концов запустил тесты с лекции и получил те же проблемы.
# По этому отформатировать код до идела не могу, т. к. не увижу результата.
#
# вот код ошибок при тестах
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.2.3\plugins\python-ce\helpers\pycharm\_jb_unittest_runner.py", line 35, in <module>
#     sys.exit(main(argv=args, module=None, testRunner=unittestpy.TeamcityTestRunner, buffer=not JB_DISABLE_BUFFERING))
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\main.py", line 100, in __init__
#     self.parseArgs(argv)
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\main.py", line 147, in parseArgs
#     self.createTests()
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\main.py", line 158, in createTests
#     self.test = self.testLoader.loadTestsFromNames(self.testNames,
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\loader.py", line 220, in loadTestsFromNames
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\loader.py", line 220, in <listcomp>
#     suites = [self.loadTestsFromName(name, module) for name in names]
#   File "C:\Users\AngaPanga\AppData\Local\Programs\Python\Python310\lib\unittest\loader.py", line 211, in loadTestsFromName
#     raise TypeError("calling %s returned %s, not a test" %
# TypeError: calling <function test_admin at 0x00000185180DB640> returned None, not a test

import pytest
import Proj as pj
import User_cls as usc


def test_project():
    assert  get_prj() == 'Проект создан'\
        , 'Проект не был создан'

def test_admin():
    assert get_admin() == check_user('Анна', '101','2')\
        , 'Админ не был создан или данные не корректны.'

def test_new_user():
    assert check_user('Саша', '115', '7') == get_new_user()\
        , 'Пользователь не был создан или данные не корректны'


def check_user(name, id, lvl):
    return usc.User(name, id, lvl)

def get_prj():
    s = str(pj.Project.load('users.csv'))
    return s

def get_admin():
    prj = pj.Project.load('users.csv')
    prj.login('Анна', '101')
    return prj.admin

def get_new_user():
    prj = pj.Project.load('users.csv')
    prj.login('Анна', '101')
    prj.add_user('Саша', '115', '7')
    return prj.users[len(prj.users) - 1]


if __name__ == '__main__':
    pytest.main(['-v'])