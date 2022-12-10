from func import *
from typing import Iterable

inp       = read_input("input")[:-1]
#  inp       = read_input("test_input")[:-1]
cycle:int = 0
def format_inp(x:str)->tuple:
    if x == "noop":
        return (x.split(" ")[0],)
    else:
        return (x.split(" ")[0],integers(x.split(" ")[1])[0])

inp = mapl(format_inp,inp)

for k in inp:
    print(k)

def computex(instructions:list)->Iterable:
    global cycle
    for i in instructions:
        if   i[0] == "noop":
            cycle+=1
            yield 0

        elif i[0] == "addx":
            cycle+=1
            yield 0
            cycle+=1
            yield i[1]

tot = 0
x=1
for i in computex(inp):
    if cycle in (20,60,100,140,180,220):
        print(x)
        tot += (cycle*x)
    x+=i
print(tot)
    
