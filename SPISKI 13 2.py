a = input("Введите первую переменную ")
znak = input("Введите знак ")
b = input("Введите вторую переменную ")
if '+' in znak:
    print(int(a) + int(b))
elif '-' in znak:
    print(int(a) - int(b))
elif '*' in znak:
    print(int(a) * int(b))
elif '/' in znak:
    print(int(a) / int(b))