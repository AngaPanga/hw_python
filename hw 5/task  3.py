# Генератор фибаначи

def gen_fibanachi(num_1, num_2):
    while True:
        num_1, num_2 = num_2, num_1 + num_2
        yield num_2

f = gen_fibanachi(0, 1)
for _ in range(10):
    print(next(f),end=' ' )