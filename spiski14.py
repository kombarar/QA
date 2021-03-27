import random

spisok1 = []
spisok2 = []
spisokall = []
spisok_bpovtorov = []
spisok_ob_2spiskov = []
spisok_unikaln= []
spisok_minmax = []

len = random.randint(1, 20)

for i in range(len):
    elfor1 = random.randint(-70, 50)
    spisok1.append(elfor1)
    elfor2 = random.randint(-70, 50)
    spisok2.append(elfor2)
    for o in spisok1:
        spisokall.append(o)
    for j in spisok2:
        spisokall.append(j)
        if j not in spisokall:
            spisok_bpovtorov.append(j)
    if elfor1 == elfor2:
        spisok_ob_2spiskov.append(elfor1) #общие для двух списков

    if elfor1 != elfor2: #уникальные числа
        spisok_unikaln.append(elfor1)
    if elfor2 != elfor1:
        spisok_unikaln.append(elfor2)


# списки для мин и макс
spisok_minmax.append(min(spisok1))
spisok_minmax.append(max(spisok1))
spisok_minmax.append(min(spisok2))
spisok_minmax.append(max(spisok1))

print("1 список", spisok1)
print("2 список", spisok2)
print("Общий", spisokall)
print("Список уникальных чисел", spisok_unikaln)
print("Список с общими для двух списков", spisok_ob_2spiskov)
print("Список обоих списков без повторения", spisok_bpovtorov)
print("минимальное и максимальное значение каждого из списков", spisok_minmax)