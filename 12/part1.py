from func import *
from collections import defaultdict

inp = read_input("input")[:-1]
inp = read_input("test_input")[:-1]
inp = list(map(list,inp))
m:list   = []
S=(0,0)
E=(0,0)
path:list= []
for i in inp:
    tmp = []
    for c in i:
        if  c=="E":
            tmp.append(ord("z")-96)
            E = (inp.index(i),i.index(c))
        elif c=="S":
            tmp.append(ord("a")-96)
            S = (inp.index(i),i.index(c))
        else:
            tmp.append(ord(c)-96)
    m.append(tmp)

def val(x,y)->bool: return x>len(m) or y >len(m[x]) or x<0 or y<0 

def DFS(x,y,path:int,visited:list)->int:
    visited.append((x,y))
    path +=1
    for xx,yy in neighbours(x,y,4):
        if (xx,yy)==S:
            return path+1

        if not(val(xx,yy) or m[xx][yy]>m[x][y]+1 or xx,yy in visited):
            path = DFS(xx,yy,path,visited)
    return path

tot=DFS(*S,0,[])
print(tot)
