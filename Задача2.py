metrs = input("Введите кол-во метров" )
santimetrs = int(metrs) * 100
decimetrs = int(metrs) * 10
millimetrs = int(metrs) * 1000
mili = int(metrs) * 0.00062
print("Это " + str(santimetrs) + " сантиметров, " + str(decimetrs) + " дециметров,"
      + str(millimetrs) + " миллиметров," + str(mili) + " миль")
