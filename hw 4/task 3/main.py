# Банкомать 2.0
from models import *

balance = 0
count_operation = 0
history_list = []

def start_menu(input_balance, count, history):
    while(True):
        print(start_msg)
        match input(input_ch_msg):
            case '1':
                input_balance = milions(input_balance)
                input_balance, count, history = input_money(input_balance, count, history)
            case '2':
                input_balance = milions(input_balance)
                input_balance, count, history = insert_money(input_balance, count, history)
            case '3':
                print(finish_msg)
                break
            case _:
                input_balance = milions(input_balance)
                print(mistake_msg)
        print(f'Ваш баланс: {input_balance} у.е. \n')
    return input_balance, count, history

def milions(balance):
    if balance >= LIMIT:
        balance *= PROCENT_RICH
    return balance

def bonus(inp_bal, count):
    if procent_bonus(count):
        return inp_bal * BONUS
    return inp_bal

def procent_bonus(c):
    if c % 3 == 0:
        return True
    return False

def check_cashe(csh):
    if csh % MULTYPLICITY == 0:
        return True
    else:
        print(error_msg)
        return False

def input_money(balance, cnt, his):
    cashe = int(input(input_msg))
    if check_cashe(cashe):
        cnt +=1
        balance += cashe
        balance = bonus(balance, cnt)
        his.append(f'На счет внесено {cashe} у.е.')
    return balance, cnt, his

def insert_money(balance, cnt, his):
    cashe = int(input(insert_msg))
    if check_cashe(cashe):
        if balance - cashe * TAX >= 0:
            cnt += 1
            balance -= (cashe * TAX)
            balance = bonus(balance, cnt)
            his.append(f'Со счета снято {cashe} у.е.')
        else:
            print(error_balance)
    return balance, cnt, his

balance, count_operation, history_list = start_menu(balance, count_operation, history_list)
print()
for el in history_list:
    print(el)