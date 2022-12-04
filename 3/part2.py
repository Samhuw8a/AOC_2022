from func import *

inp = read_input("input")
#  inp = read_input("test_inp")

def find_same(v1,v2,v3)->tuple:
    for i in v1:
        if i in v2 and i in v3:
            same = i
    s = ord(same)- 64+26 if same.isupper() else ord(same)-96
    return s,same


score =0
for i in range(0,len(inp),3):
    s,same =find_same(inp[i],inp[i+1],inp[i+2])
    #  print(s)
    score +=s

print(score)
