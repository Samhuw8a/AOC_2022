from func import *

inp = read_input("input")
inp = mapl(lambda x: tuple(x.split(" ")),inp)

def won(x:str,y:str)->int:
    if x == "A":
        if y == "X":return 0
        elif y == "Y":return 1
        elif y == "Z":return -1
    elif x == "B":
        if y == "X":return -1
        elif y == "Y":return 0
        elif y == "Z":return 1

    elif x == "C":
        if y == "X":return 1
        elif y == "Y":return -1
        elif y == "Z":return 0

    print("ERROR")
    return 0

s:int = 0
for got,played in inp:
    w = won(got,played)
    if played=="X"   : s+=1
    elif played=="Y" : s+=2
    elif played=="Z" : s+=3

    if w == 1        : s+=6
    elif w == 0      : s+=3
    
print(s)
