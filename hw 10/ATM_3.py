import msg_dict


class Atm:
    __START_NUM = 0
    __STEP = 1
    __MAX_CUNT = 3
    __UNRICH_LIMIT = 5000000
    __PROCENT_RICH = 0.9
    __MULTYPLICITY = 50
    __BONUS = 1.03
    __TAX = 1.015
    def __init__(self):
        self.__balance = self.__START_NUM
        self.__count_operations = self.__START_NUM
        self.__history_list = []
        print(msg_dict.start_msg)

    def get_balance(self):
        return self.__balance

    def rich_tax(self):
        if self.__balance >= self.__UNRICH_LIMIT:
            self.__balance *= self.__PROCENT_RICH

    def __check_cashe(self, ins_sum):
        if ins_sum % self.__MULTYPLICITY == 0:
            return True
        return False

    def __bonus(self):
        if self.__count_operations % self.__MAX_CUNT == self.__START_NUM:
            self.__balance *= self.__BONUS

    def __ap_history(self, msg, inp_sum):
        self.__history_list.append(msg + str(inp_sum))

    def input_money(self, inp_cashe):
        self.rich_tax()
        if self.__check_cashe(inp_cashe):
            self.__balance += inp_cashe
            self.__count_operations += self.__STEP
            self.__bonus()
            self.__ap_history(msg_dict.inp_msg, inp_cashe)
            return msg_dict.out_balance + str(self.get_balance())
        else:
            return msg_dict.cashe_error

    def insert_money(self, ins_cashe):
        self.rich_tax()
        if self.__check_cashe(ins_cashe) and self.__balance > ins_cashe * self.__TAX:
            self.__balance -= ins_cashe * self.__TAX
            self.__count_operations += self.__STEP
            self.__bonus()
            self.__ap_history(msg_dict.ins_msg, ins_cashe)
            return msg_dict.out_balance + str(self.get_balance())
        else:
            return msg_dict.cashe_error

    def history(self):
        self.rich_tax()
        for el in self.__history_list:
            print(el)


atm = Atm()
while(True):
        match input(msg_dict.input_ch_msg):
            case '1':
                cashe = int(input(msg_dict.input_msg))
                print(atm.input_money(cashe))
            case '2':
                cashe = int(input(msg_dict.insert_msg))
                print(atm.insert_money(cashe))
            case '3':
                atm.history()
            case '4':
                print(msg_dict.finish_msg)
                break
            case _:
                atm.rich_tax()
                print(msg_dict.mistake_msg)