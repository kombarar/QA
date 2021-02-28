vvod = int(input())
if 1<= vvod <= 100:
    if vvod % 3 == 0:
        print("Fizz")
    if vvod % 5 == 0:
        print("Buzz")
    if (vvod % 3 != 0) and (vvod % 5 != 0):
        print(vvod)
else :
    print("Число не в диапазоне!")
