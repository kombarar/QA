naib = 0
crednee = 0
minim = 0
naz1 = ""
naz2 = ""
naz3 = ""
kol_vidov = int(input("Введите кол-во видов цветов в букете: "))
for i in range(kol_vidov):
    name = input("Название цветка: ")
    kol_v_bukete = int(input("Введите кол-во самих цветов в букете: "))
    if (kol_v_bukete>naib):
        minim = crednee
        naz3 = naz2
        crednee = naib
        naz2 = naz1
        naib = kol_v_bukete
        naz1 = name
    if (kol_v_bukete<naib) and (kol_v_bukete>crednee):
        minim=crednee
        naz3 = naz2
        crednee = kol_v_bukete
        naz2 = name
    if (kol_v_bukete<crednee) and (kol_v_bukete>minim):
        minim = kol_v_bukete
        naz3 = name
print(naib, naz1)
print(crednee, naz2)
print(minim, naz3)