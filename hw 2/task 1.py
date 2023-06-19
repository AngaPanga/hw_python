balance = 0
count_operation = 0

def start_menu(bal, count):
    while(True):
        print('~~~ Банкомат ~~~\n'
              'Добропожаловать.\n'
              'Ваш баланс:',bal,'\n'
                                     '1. Пополнить баланс\n'
                                    '2. Снять наличные\n'
                                    '3. Завершить работу')
        match input('Выберите действие (№): '):
            case '1':
                bal = milions(bal)
                bal, count = input_money(bal, count)
            case '2':
                bal = milions(bal)
                bal, count = insert_money(bal, count)
            case '3':
                print('Благодарим за использование наших услуг.')
                break
            case _:
                bal = milions(bal)
                print('\n   Ошибка ввода! Повторите ввод.\n')
    return bal, count

def milions(b):
    LIMIT = 5000000
    if b >= LIMIT:
        b -= b * 0.1
    return b

def procent(c):
    if c % 3 == 0:
        return True
    else:
        return False

def check_cashe(csh):
    if csh % 50 == 0:
        return True
    else:
        print('\nВведена недопустимая сумма!\n')
        return False

def input_money(b, cnt):
    cashe = int(input('\nВведите сумму для внесения: '))
    if check_cashe(cashe):
        cnt +=1
        b += cashe
        if procent(cnt):
            b *= 1.03
    return b, cnt

def insert_money(b, cnt):
    cashe = int(input('\nВведите сумму для снятия: '))
    if check_cashe(cashe):
        if b - cashe * 1.015 >= 0:
            cnt += 1
            b = b - (cashe * 1.015)
            if procent(cnt):
                b *= 1.03
        else:
            print('\nНа счету не достаточно средств!')
    return b, cnt


balance, count_operation = start_menu(balance, count_operation)