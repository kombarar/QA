a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
sumch = 0 #сумма четных
sumnch = 0 #сумма не четных
sum9 = 0 #сумма кратных 9
#сумма четных
for i in range(a, b+1):
    if i%2 == 0:
        sumch +=i

    if i%2 != 0:
        sumnch +=i

    if i%9 == 0:
        sum9 +=i
print("Сумма четных",sumch)
print()
print("Сумма нечетных",sumnch)
print()
print("Сумма чисел, кратных 9",sum9)