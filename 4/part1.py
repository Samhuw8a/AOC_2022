from func import *

inp = read_input("input")
#  inp = read_input("test_input")

inp = mapl(lambda x :x.split(","),inp)
for i in inp:
    inp[inp.index(i)] = mapt(lambda x : x.split("-"),i)

def is_contained(p)->bool:
    p1,p2 = p
    i1,i2 = digits(p1)
    r1=list(range(i1,i2+1))
    i3,i4 = digits(p2)
    r2=list(range(i3,i4+1))
    #  if i1<=i3 and i2>=i4:
    #      print(i1,i2,"-",i3,i4)
    #      return True
    #  if i3<=i2 and i4>=i2:
    #      print(i1,i2,"-",i3,i4)
    #      return True
    #  return False
    check =  all(item in r2 for item in r1) or all(i in r1 for i in r2)
    return check

tot = 0 
for i in inp:
    if is_contained(i):
        tot +=1
print(tot)
