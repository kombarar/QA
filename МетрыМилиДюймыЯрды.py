print("Введите кол-во метров")
metrs = int(input())
print("Перевести метры в мили, дюймы или ярды?")
choice = input()
if choice == "мили":
    print(metrs* 0.00062)
else :
    if choice == "дюймы":
        print(metrs*39.37)
    else:
        if choice=="ярды" :
            print(metrs * 1.09)
        else:
            print("Выберете единицу измерения из представленных выше!")