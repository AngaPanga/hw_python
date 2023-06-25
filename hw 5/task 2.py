# Генератор зарплат в словарь

ar_1 = ['petr', 'ivan', 'sasha']
ar_2 = ['15000', '20000', '30000']
ar_3 = ['10.25%', '15.42%', '12.55%']

res_dict = {val[0] : int(val[1])*(float(val[2].replace('%','')))/100 for val in zip(ar_1, ar_2, ar_3)}

for key, el in res_dict.items():
    print(key, '-', el)