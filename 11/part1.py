from func import *

inpt = read_input("input",sep="\n\n")
#  inpt = read_input("test_input",sep="\n\n")
inpt = mapl(lambda x: x.split("\n"),inpt)
inp  = {}

def op(old:int,ip:str)->int:
    cmd    = ip.split(" ")
    first  =old if cmd[0]=="old" else int(cmd[0])
    second =old if cmd[2]=="old" else int(cmd[2])
    if   cmd[1]=="*":return first * second
    elif cmd[1]=="+":return first + second
    print("error")
    return 0

for i in inpt:
    inp[i[0].split(" ")[1].strip(": ")]={
        "items"    :list(integers(i[1].split(":")[1])),
        "operation":i[2].split(":")[1].split("= ")[1],
        "test"     :integers(i[3].split(":")[1])[0],
        "true"     :integers(i[4].split(":")[1])[0],
        "false"    :integers(i[5].split(":")[1])[0],
        "times"    :0
    }
#  for i in inp.values():
#      print(i)

for _ in range(20):
    for k,m in inp.items():
        nm = m["items"]
        for n,i in enumerate(nm):
            #  print(m["items"])
            m["times"]+=1
            j = op(i,m["operation"])
            j = j//3
            print(j)
            #  print(k,i,j)
            if j % m["test"]==0:
                #  print(k,j,m["test"],j//m["test"])
                nxt=m["true"]
            else:
                #  print(k,j,m["test"],j//m["test"])
                nxt=m["false"]

            inp[str(nxt)]["items"].append(j)
            #  print(k,nxt,j)
            #  print(inp[str(nxt)]["items"])

        inp[k]["items"]=[]

print() 
for i in inp:
    print(inp[i]["items"])
tot = []
for i in inp:
    tot.append(inp[i]["times"])

tot.sort(reverse=True)

print(tot[0]*tot[1])
