
print("Введите продажи за месяц первого менеджера")
manager1 = int(input())
zp1 = 200

print("Введите продажи за месяц второго менеджера")
manager2 = int(input())
zp2 = 200
print("Введите продажи за месяц третьего менеджера")
manager3 = int(input())
zp3 = 200

list1 = [manager1,manager2,manager3]
list2 = []



#if (manager1 > manager2) and (manager1 > manager3):
#    zp1 +=200 #выписали премию


#if (manager2 > manager1) and (manager2 > manager3):
#    zp2 += 200

#if (manager3 > manager1) and (manager3 > manager2):
#    zp3 += 200
listzp = []

for x in list1: # list2 содержит проценты от продаж
        if x < 500:
            c = x * 0.03 + 200
            list2.append(c)
        else:
            if (500 <= x <= 1000):
                c = x * 0.05 + 200
                list2.append(c)

            else:
                if x>1000:
                    c = x * 0.08 + 200
                    list2.append(c)
print(list2)
for o in list2:
    if (list2[0] > list2[1]) and (list2[0] > list2[2]):
        listzp.append(list2[0]+200) #выписали премию
    if (list2[1] > list2[0]) and (list2[1] > list2[2]):
        listzp.append(list2[1]+200)
    if (list2[2] > list2[0]) and (list2[2] > list2[1]):
        listzp.append(list2[2]+200)
print(listzp)
