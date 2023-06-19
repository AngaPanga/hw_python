# Возвращение словаря с хешом

def dict_hash(**kwargs):
    res = {}
    for key, el in kwargs.items():
        if el.__hash__ == None:
            el = str(el)
        res[el] = key
    return res

print(dict_hash(a = 5, b = [5, 6]))
