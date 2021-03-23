stroka = input("Введите строку ")
poisk = input("Введите символ для поиска ")
start = -1
count = 0
while True:
    start = stroka.find(poisk, start+1)
    if start == -1:
        break
    count += 1
print(count)