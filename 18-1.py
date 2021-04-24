def isEqual(string, symbol, index):
    if len(symbol) != 1:
        raise ValueError("Символ должен быть длиной 1")
    if index >= len(string):
        raise ValueError("Индекс за пределами строки")
    return string[index] == symbol

stroka = input()
symbol = input()

count = 0
i = 0

for i in range(0, len(stroka) - 1):
    try:
        if isEqual(stroka, symbol, i):
            count += 1
    except Exception as e:
        print("Произошла ошибка: " + str(e))
        exit(0)
for i in range(0, len(stroka)):

    if stroka[i] == symbol:
        res = i + 1
        break

print(f'Символ встречается в строке : {count} раз')
print(f'Позиция, на которой встречается в первый раз - {res} ')


