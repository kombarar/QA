import math
print("Введите цену единицы товара")
cena = int(input())
print("Введите кол-во товара")
kolvo = int(input())
itog = (cena*kolvo)
if kolvo>=5:
   skidka = (itog * 0.25)
   itogwithsk = itog - skidka
   print(math.floor(itogwithsk))
else:
   print(itog)
if kolvo>=10:
   itog = (cena * kolvo)
   skidka = (itog * 0.5)
   itogwithsk = itog - skidka
   print(math.floor(itogwithsk))
