# Проверка на существование треугольника

a = int(input('Введите длину стороны A: '))
b = int(input('Введите длину стороны B: '))
c = int(input('Введите длину стороны C: '))

if a + b < c or a + c < b or b + c < a:
    print('Треугольника не существует!')
else:
    match a, b, c:
        case a, b, c if a == b == c:
            print('Треугольник равносторонний!')
        case a, b, c if a == b or a == c or b == c:
            print('Треугольник равнобедренный!')
        case a, b, c if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2:
            print('Треугольник прямоугольный!')
        case _ :
            print('Треугольник разносторонний!')
