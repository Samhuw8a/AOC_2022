from collections.abc import Iterable
from func import *

inp = read_input("input")
# inp = read_input("test_input")
m = [mapl(int,list(i))for i in inp[:-1]] 
outside:int =len(m)*2+(len(m[0])-2)*2

def line_neg_x(x:int,y:int)->Iterable:
    nx=x
    while nx != 0 :
        nx-=1
        yield (nx,y)

def line_inc_x(x:int,y:int)->Iterable:
    nx=x
    while nx != len(m)-1 :
        nx+=1
        yield (nx,y)

def line_neg_y(x:int,y:int)->Iterable:
    ny=y
    while ny != 0 :
        ny-=1
        yield (x,ny)

def line_inc_y(x:int,y:int)->Iterable:
    ny=y
    while ny != len(m)-1 :
        ny+=1
        yield (x,ny)

def is_vis(x:int,y:int)->bool:
    v = m[x][y]
    nxvis = True
    for nx,ny in line_neg_x(x,y):
        if m[nx][ny] >=v:
            nxvis= False
    nyvis = True
    for nx,ny in line_neg_y(x,y):
        if m[nx][ny] >=v:
            nyvis= False
    ixvis = True
    for nx,ny in line_inc_x(x,y):
        if m[nx][ny] >=v:
            ixvis= False
    iyvis = True
    for nx,ny in line_inc_y(x,y):
        if m[nx][ny] >=v:
            iyvis= False
    return nxvis or nyvis or ixvis or iyvis

tot = 0
for i in range(1,len(m)-1):
    for j in range(1,len(m[i])-1):
        if is_vis(i,j):
            tot +=1

# print(tot)
print(tot+outside)

