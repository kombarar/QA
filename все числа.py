a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
#вывести все числа диапазона
for i in range(a, b+1):
   print(i, end=' ')
print()
#вывести все числа диапазона в обратном порядке
for i in range(b, a-1, -1):
   print(i, end=' ')
print()
#вывести все числа кратные 7
for i in range(a, b):
   if i % 7 == 0:
       print(i, end=' ')
print()
#вывести все числа кратные 5
for i in range(a, b):
   if i % 5 == 0:
       print(i, end=' ')