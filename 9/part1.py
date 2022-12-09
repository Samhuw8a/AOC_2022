from func import *
from collections import defaultdict

inp = read_input("input")[:-1]
inp = read_input("test_input")[:-1]
inp = mapl(lambda x: (x.split()[0],int(x.split()[1])), inp)
#  print(inp)
HX,HY = 0,0
TX,TY = 0,0
def inc_tail(x:int,y:int,d:str)->tuple:
    if (x,y) in list(neighbours(HX,HY,9)):
        return x,y
    else:
        x -= sign(HX-x)
        y -= sign(HY-y)
    return x,y

def inc_head(x:int,y:int,d:str)->tuple:
    if    d == "R": y+=1
    elif  d == "L": y-=1
    elif  d == "D": x+=1
    elif  d == "U": x-=1
    return x,y

def make_move(direction:str,amount:int, tail:defaultdict)->defaultdict:
    global HX,HY
    global TX,TY

    TX,TY = HX,HY
    for _ in range(amount):
        HX,HY = inc_head(HX,HY,direction)
        TX,TY = inc_tail(TX,TY,direction)
        tail[abs(TX),abs(TY)]=True
    return tail


tail:defaultdict = defaultdict(bool)
for d,m in inp:
    tail=make_move(d,m,tail)

print(tail)
tot = sum(1 for i in tail.values() if i)
print(tot)
