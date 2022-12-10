from func import *
from typing import Iterable

inp          = read_input("input")[:-1]
# inp          = read_input("test_input")[:-1]
screen:list  = [["." for _ in range(40)]for _ in range(6)]
cycle:int    = 0
x:int        = 0
sprite:tuple = (x,x+1,x+2)

def format_inp(x:str)->tuple:
    if x == "noop":
        return (x.split(" ")[0],)
    else:
        return (x.split(" ")[0],integers(x.split(" ")[1])[0])
inp = mapl(format_inp,inp)

def prt_sc()->None:
    for i in screen:
        for j in i:
            print(j,end="")
        print()

def convert_xy(cyc:int)->tuple:
    x = cyc//40
    y = cyc - (x*40)
    return x,y

def computex(instructions:list)->Iterable:
    global cycle
    global screen
    for i in instructions:
        if   i[0] == "noop":
            cx,cy = convert_xy(cycle)
            screen[cx][cy]="#" if cy in sprite else "."
            cycle+=1
            yield 0

        elif i[0] == "addx":
            cx,cy = convert_xy(cycle)
            screen[cx][cy]="#" if cy in sprite else "."
            cycle+=1
            yield 0
            cx,cy = convert_xy(cycle)
            screen[cx][cy]="#" if cy in sprite else "."
            cycle+=1
            yield i[1]

for i in computex(inp):
    x+=i
    xy = x-(x//40*40)
    sprite = (xy,xy+1,xy+2)
    
prt_sc()
