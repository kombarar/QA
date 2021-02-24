print("Введите 4 положительных числа")
chislo1 = int(input())
chislo2 = int(input())
chislo3 = int(input())
chislo4 = int(input())
if chislo1 > chislo2 and chislo1 > chislo3 and chislo1>chislo4:

   print('Номер наибольшего числа = 1, а число - ', chislo1)

elif chislo2 > chislo1 and chislo2 > chislo3 and chislo2 > chislo4:

   print('Номер наибольшего числа = 2, а число - ', chislo2)

elif chislo3 > chislo1 and chislo3 > chislo2 and chislo3 > chislo4:

   print('Номер наибольшего числа = 3, а число - ', chislo3)

elif  chislo4 > chislo1 and chislo4 > chislo2 and chislo4 > chislo3:

   print('Номер наибольшего числа = 4, а число - ', chislo4)
