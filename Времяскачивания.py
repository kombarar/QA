print("Введите размер файла в Гб")
number1 = int(input())
print("Введите скорость интернет-соединения в битах в секунду")
number2 = int(input())
print("Посчитать, за сколько часов или минут, или секунд скачается файл.")
choice = input()
if choice == "часы":
    bit = number1*1024 #Гб в Мб
    skorost = number2*20.00045 #бит в сек перевести в МБ в час
    print(bit/skorost)
else:
    if choice == "минуты":
        bit1 = number1 * 1024
        skorost1 = number2 * (7.5 * 0.000001) # бит в сек перевести в МБ в минуту
        print(bit1/skorost1)
    else:
        forsec = number1*8589934592
        print(forsec/number2)