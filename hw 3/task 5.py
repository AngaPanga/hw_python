from random import randint
RND_N = 20

ar = []
ar_2 = []
for _ in range(RND_N):
    ar.append(randint(1, 5))
print(*ar)

for el in ar:
    if el not in ar_2:
        ar_2.append(el)
print(*ar_2)