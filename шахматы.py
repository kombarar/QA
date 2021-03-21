from __future__ import print_function
c = int(input("Размер клетки"))

for i in range(8):
    for j in range(8):
       for k in range(c):
            if int(i) % 2 == 0:
                if int(j) % 2 == 0:
                    print("*", end=' ')
                else:
                    print("-", end=' ')
            else:
                if int(j) % 2 != 0:
                    print("*", end=' ')
                else:
                    print("-", end=' ')
    print()