print("Введите с клавиатуры номер месяца (от 1 до 12)")
month = int(input())
if month == 1 or month == 12 or month == 2:
    print("Winter")
else :
    if 3<=month<=5 :
        print("Spring")
    else:
        if 6<=month<=8 :
            print("Summer")
        else:
            if 9 <= month <= 11:
                print("Autumn")
            else: print("Ошибка! Вы ввели число не из диапозона от 1 до 12, проверьте!")