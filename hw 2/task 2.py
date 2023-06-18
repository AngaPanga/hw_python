num_user = int(input('Введи число: '))
ar = []
BASE = 16
while num_user > 0:
    c = num_user % BASE
    match c:
        case 10:
            ar.append('A')
        case 11:
            ar.append('B')
        case 12:
            ar.append('C')
        case 13:
            ar.append('D')
        case 14:
            ar.append('E')
        case 15:
            ar.append('F')
        case _:
            ar.append(c)
    num_user //= BASE
ar.reverse()
ar = map(str, ar)
s = ''.join(ar)
print(s)