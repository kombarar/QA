spisok = input("Введи список чисел: ").split(',')
result = [int(item) for item in spisok]
def sortir(result):
    result.sort()
    print(result)

def pux(result):
    perestanovka_on = True
    while perestanovka_on:
        perestanovka_on = False
        for i in range(len(result) - 1):
            if int(result[i]) > int(result[i + 1]):
                result[i], result[i + 1] = result[i + 1], result[i]
                perestanovka_on = True
    print(result)

pux(result)
print("Отсортировано пузырьком функцией")
sortir(result)
print("Отсортировано встроенной функцией")