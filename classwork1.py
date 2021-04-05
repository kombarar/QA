spisok = input("Введи список чисел: ").split(',')
result = [int(item) for item in spisok]
def maxim(result):
    print("максимальное число - ", max(result))
maxim(result)