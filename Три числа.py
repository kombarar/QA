number1 = int(input())
number2 = int(input())
number3 = int(input())
print("Вывести на экран сумму трёх чисел или произведение?")
choice = input()
if choice == "сумму" or choice == "сумма":
    print(number1+number2+number3)
else:
    print(number1*number2*number3)