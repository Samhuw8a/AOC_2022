from func import *
inp = read_input("input",sep="\n\n")
m:list = [sum(digits(i.split("\n"))) for i in inp]
m.sort()
print(m[-1])
