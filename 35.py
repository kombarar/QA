a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
for i in range(a, b+1):
    if i % 3 == 0:
        print("Fizz")
    if i % 5 == 0:
        print("Buzz")
    if (i % 3 != 0) and (i % 5 != 0):
        print(i)
else :
    print("Число не в диапазоне!")
