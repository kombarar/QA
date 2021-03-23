stroka: str = input("Введите текст ")
count_cifra = 0
count_bukva: int = 0
for i in stroka:
    if i.isdigit():
        count_cifra += 1
    if i.isalpha():
        count_bukva += 1
print("Кол-во цифр в строке", count_cifra)
print("Кол-во букв в строке", count_bukva)
