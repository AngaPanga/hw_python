CHET = 2
STEP = 1
ar_1 = [5, 6, 1, 8, 2, 3, 7, 9, 9, 10, 55, 55, 13]
ar_2 = []
count = 1

for el in ar_1:
    if el % CHET != 0:
        ar_2.append(str(count) + '. ' + str(el))
        count += STEP

for val in ar_2:
    print(val)