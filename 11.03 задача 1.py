print("Выберете валюту, которую надо перевести: рубли, евро, доллары?")
valuta = input()
print("Выбирает валюту в которую надо произвести пересчёт: рубли, евро, доллары?")
choice = input()
print("Введите кол-во")
kolvo = int(input())
if valuta == "рубли":
    if choice == "евро":
        print(kolvo/90, choice)
    else:
        if choice=="доллары" :
            print(kolvo/80, choice)
        else:
            print("Вы ошиблись, выберете валюту не равную исходной")
else :
    if valuta == "евро":
        if choice == "рубли":
            print(kolvo * 90, choice)
        else:
            if choice == "доллары":
                print(kolvo / 0.85, choice)
            else:
                print("Вы ошиблись, выберете валюту не равную исходной")
    else:
        if valuta == "доллары":
            if choice == "рубли":
                print(kolvo * 80, choice)
            else:
                if choice == "евро":
                    print(kolvo * 0.85, choice)
                else:
                    print("Вы ошиблись, выберете валюту не равную исходной")