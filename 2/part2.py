from func import *

inp = read_input("input")
inp = mapl(lambda x: tuple(x.split(" ")),inp)

def won(x:str,y:str)->int:
    if y == "X":
        if x == "A":return 3
        elif x == "B":return 1
        elif x == "C":return 2

    elif y == "Y":
        if x == "A":return 1
        elif x == "B":return 2
        elif x == "C":return 3

    elif y == "Z":
        if x == "A":return 2
        elif x == "B":return 3
        elif x == "C":return 1

    print("ERROR")
    return 0

s:int = 0
for got,played in inp:
    w = won(got,played)
    if played=="X"   : s+=0
    elif played=="Y" : s+=3
    elif played=="Z" : s+=6
    s+=won(got,played)
    
print(s)
