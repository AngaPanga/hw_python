class AccessExp(Exception):
    def __str__(self):
        return f'Ошибка доступа! Такого пользователя нет.'


class LevelExp(Exception):
    def __str__(self):
        return f'Ошибка! Уровень доступа не достаточен.'