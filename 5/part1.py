from func import *

inp = read_input("input",sep="\n\n")
#  inp = read_input("test_input",sep="\n\n")
cargo,inst=inp
inst = inst.split("\n")
inst=mapt(lambda x: integers(x),inst)
cargo = cargo.split("\n")
cargo = mapt(lambda x: x.strip().split(" "),cargo)
stack:dict = {}
for i,s in cargo:
    stack[int(i)] = list(s)

#  print(inst)
def move(n:int, frm:int , to:int )->None:
    global stack
    for _ in range(n):
        tmp = stack[frm][-1]
        if stack[frm]:
            del stack[frm][-1]
        stack[to].append(tmp)

for n,frm,to in inst:
    move (n,frm,to)

for k,i in stack.items():
    #  print(i)
    print(i[-1],end="")
print()
