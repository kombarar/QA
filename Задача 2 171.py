print("Введите диапазон значений")

a = int(input("Введите начало диапазона "))
b = int(input("Введите конец диапазона "))
for i in range(a, b + 1):
   flag = True
   for f in range(1, i):
       if i % f == 0: #Если число не простое, то оно не записывается
           flag = False
           break
   if flag:
        print(i, end=' ')




