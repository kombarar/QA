import random
ra = (int(random.uniform(1, 500)))
print('Число загадано от 1 до 500. Угадай!')
print("Твоё число:")
popitki = 1
number = int(input())
x = True
while (x == True):
        while number != ra:
            if number == 0:
                print('Вы проиграли. Число было', ra);
                break
            if number < ra:
                popitki += 1
                print("Не угадал. Число больше.Введите число снова")
                number = int(input())
            if number > ra:
                popitki += 1
                print("Не угадал. Число меньше.Введите число снова")
                number = int(input())
        if number == ra:
            x = False
            print('Ты угадал! Это число', ra)
            print('Тебе потребовалось попыток:', popitki)





