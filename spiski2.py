list = []
a = []
j =0
new_str = ""
for i in range(1):
    slovo = input()
    list.append(slovo)
for o in list:
    for i in range(len(o)-1,-1,-1):
        new_str+=o[i]
    if new_str==o:
        print("YES")
    else: print("NO")
