
def fnc(a, b):
    for i in range(a + 1, b):
        print(i, end=" ")
        if i % 2 == 1:
            print(i)

print(fnc(5,12))
