print("Введите диапазон значений")
a = int(input("Введите начало диапазона "))
b = int(input("Введите конец диапазона "))
print("Ниже показана таблица умножения в этом диапазоне")
for i in range(a, b+1):
     print(*range(i, i*10+1, i), sep='\t') #sep — Cтрока, вставляемая между значениями





