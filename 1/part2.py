from func import *

inp = read_input("input",sep="\n\n")
m = []
for i in inp:
    m.append(sum(mapl(int, i.split("\n"))))


m.sort()
print(m[-1],m[-2],m[-3])
print(sum((m[-1],m[-2],m[-3])))
