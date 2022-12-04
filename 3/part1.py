from func import *

inp = read_input("input")
#  inp = read_input("test_inp")

def find_same(l:str)->int:
    l1 = l[:len(l)//2]
    l2 = l[len(l)//2:]
    for i in l1:
        if i in l2:
            same= i
    #  print(same)
    s = ord(same)- 64+26 if same.isupper() else ord(same)-96
    return s


score =0
for i in inp:
    score += find_same(i)
print(score)
