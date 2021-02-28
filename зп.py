
print("Введите продажи за месяц первого менеджера")
manager1 = int(input())
zp1 = 200
print("Введите продажи за месяц второго менеджера")
manager2 = int(input())
zp2 = 200
print("Введите продажи за месяц третьего менеджера")
manager3 = int(input())
zp3 = 200
if (manager1 > manager2) and (manager1 > manager3):
    zp1 +=200 #выписали премию
if (manager2 > manager1) and (manager2 > manager3):
    zp2 += 200
if (manager3 > manager1) and (manager3 > manager2):
    zp3 += 200

if manager1<500:
    zp1+=manager1*0.03
elif 500 <= manager1 <= 1000:
    zp1+=manager1*0.05
elif manager1 > 1000:
    zp1+=manager1*0.08
print(zp1)
if manager2<500:
    zp2+=manager2*0.03
elif 500 <= manager2 <= 1000:
    zp2+=manager2*0.05
elif manager2 > 1000:
    zp2+=manager2*0.08
print(zp2)
if manager3<500:
    zp3+=manager3*0.03
elif 500 <= manager3 <= 1000:
    zp3+=manager3*0.05
elif manager3 > 1000:
    zp3+=manager3*0.08


print(zp3)