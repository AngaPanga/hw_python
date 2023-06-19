# Транспонирование матрицы

START = 0

def trns_matrix(ar, s):
    res_ar = []
    for j in range(len(ar[s])):
        box = []
        for i in range(len(ar)):
            box.append(ar[i][j])
        res_ar.append(box)
    return res_ar

array = [[0,0,0,0],
         [1,1,1,1]]

array_2 = trns_matrix(array, START)

for el in array_2:
    print(*el)
