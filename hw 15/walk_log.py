# Вобщем несколько моментов:
# 1. По идее я поступил, набрал 196 за все 3 предмета. На 2 месте среди моей категории.
#    Зачисление только 07.08.2023
# 2. Спустя несколько дней тесты заработали хотя ничего не делал
# 3. Не согласен с оценкой за 14. По условию задачи нужно было сделать от 3 тестов.
# Три теста я сделал но проверить не мог.
# В связи с этим не делал больше тестов, и в условиях задачи не было сказано какие виды тестов делать
# Согласен, что за не красивый код можно было снизить на бал оценку (хотя и была причина плохого кода указана)
# Но "удоволетворительно как то жестоко. Либо я что то не понимаю?
#
# В данном дз целенаправленно упрощен код от исходного!
# Вижу недостаток в структуре "сообщеня лога", более элегантного решения не нашел.
# Как правильнее?
# Да и есть слабое место если файл будет без расширения, программа ломается
# ни стал усложнять написанием функции проверки имени файла.

import os
import logging
import sys

logging.basicConfig(
    filename="logs.log",
    filemode='a',
    encoding="Utf-8",
    level=logging.INFO,
)

logger = logging.getLogger()

def walk_dir(start_folder):
    pth = os.path.normpath(start_folder)
    head_list = ('Name obj', 'Parent dir', 'Type', 'Ext')
    global_list_obj = []
    for address, dirs, files in os.walk(pth):
        for file in files:
            n_file, ext = str(file).split('.')
            temp_dict = {
                head_list[0] : n_file,
                head_list[1] : os.path.basename(address),
                head_list[2] : 'file',
                head_list[3] : ext
                }
            global_list_obj.append(temp_dict)
            logger.info(f'{head_list[0]} - {temp_dict[head_list[0]]}; '
                        f'{head_list[1]} - {temp_dict[head_list[1]]}; '
                        f'{head_list[2]} - {temp_dict[head_list[2]]}; '
                        f'{head_list[3]} - {temp_dict[head_list[3]]}; ')
        for th_dir in dirs:
            temp_dict = {
                head_list[0] : th_dir,
                head_list[1] : os.path.basename(address),
                head_list[2] : 'directory'
                }
            global_list_obj.append(temp_dict)
            logger.info(f'{head_list[0]} - {temp_dict[head_list[0]]}; '
                        f'{head_list[1]} - {temp_dict[head_list[1]]}; '
                        f'{head_list[2]} - {temp_dict[head_list[2]]}; ')
    print(global_list_obj)

if __name__ == '__main__':
    _, path_dir = sys.argv
    # path_dir = 'D:\учеба\ДЗ и прочее\ДЗ Python специализация\hw_python\hw 15'
    walk_dir(path_dir)