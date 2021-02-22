import math
diametr = int(input())
print("Посчитать площадь или периметр?")
k = input()
if k == "площадь":
    print(((diametr**2)/4)*math.pi)
else:
    print(diametr*math.pi)
