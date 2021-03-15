print("Введите ниже число и выберите в меню дальнейшее действие")
while True:
    a = (input("Введите число "))
    while True:
        menu = int(input(
        '1 - Длина введенного числа'
        '\n'
        '2 - Сумма цифр в введенном числе'
        '\n'
        '3 - Определить кол-во нулей в введенном числе'
        '\n'
        '0 - Выход '))
        if menu == 1:
            print("Длина числа равна: ", len(str(a)))
        elif menu == 2:
            sum = 0
            while (a != 0):
                sum = sum + int(a) % 10
                a = int(a) // 10
            print("Сумма цифр числа равна: ", sum)
        elif menu == 3:
            k = 0
            for i in range(len(str(a))):
                if i == 0:
                    k = k + 1
            print("Нулей в числе - ", k)
        elif menu == 0:
            break
