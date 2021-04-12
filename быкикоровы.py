import random
print("Программа загадывает четрехзначное число. Вам необходимо его угадать. Дерзайте!")
n=str(random.randint(1000, 9999))
bull = 0
cow = 0

while True:
    text = input("Введите число или стоп для выхода: ")
    if text == "стоп":
        print("Выход из программы! До встречи! Загадано было", n)
        break
    elif text == n:
        print("Победа")
    else:
        for elem in str(text):
            if elem in str(n):
                bull+=1
        for i in range(4):
            if str(text[i]) == str(n[i]):
                cow+=1
        print("Попробуйте еще")
        print("Колличество быков ", bull)
        print("Колличество коров ", cow)

