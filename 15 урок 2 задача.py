
def fnc(dlina, napravl, simvol):
    for i in range(1, dlina):
        if napravl =="вертикально":
            print(simvol)
        if napravl =="горизонтально":
            print(simvol, end=' ')
fnc(10,"горизонтально", "*")

