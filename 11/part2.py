from func import *

inpt       = read_input("input",sep= "\n\n")
#  inpt       = read_input("test_input",sep= "\n\n")
inpt       = mapl(lambda x: x.split("\n"),inpt)
inp:dict   = {}
items:list = []
def op(old:int,ip:str)->int:
    cmd    = ip.split(" ")
    first  =old if cmd[0]=="old" else int(cmd[0])
    second =old if cmd[2]=="old" else int(cmd[2])
    if   cmd[1]=="*":return first * second
    elif cmd[1]=="+":return first + second
    print("error")
    return 0


for i in inpt:
    items.append(list(integers(i[1].split(":")[1])))
    inp[i[0].split(" ")[1].strip(": ")]={
        #  "items"    :list(integers(i[1].split(":")[1])),
        "operation":i[2].split(":")[1].split("= ")[1],
        "test"     :integers(i[3].split(":")[1])[0],
        "true"     :integers(i[4].split(":")[1])[0],
        "false"    :integers(i[5].split(":")[1])[0],
        "times"    :0
    }
#  for i in inp.values():
#      print(i)

for _ in range(10000):
    for k,m in inp.items():
        nm = items[int(k)]
        for n,i in enumerate(items[int(k)]):
            m["times"]+=1

            j = op(i,m["operation"])

            if j % m["test"]==0:
                nxt=m["true"]
            else:
                nxt=m["false"]

            items[nxt].append(j)

        items[int(k)]=[]

print() 
#  for i in items:
#      print(i)
tot = []
for i in inp:
    #  print(inp[i]["times"])
    tot.append(inp[i]["times"])

tot.sort(reverse=True)

print(tot[0]*tot[1])
