dlina = int(input())
symbol = input()
bool = input()

def draw_square(dlina, symbol, bool):
    alls = 0
    for i in dlina+1:
        alls += symbol
    if bool == "false":
        vnutri = symbol + " " * (dlina - 2) + symbol
    else:
        vnutri = alls
    print(alls)
    for i in range(dlina - 2):
        print(vnutri)
    print(alls)

draw_square(dlina, symbol, bool)