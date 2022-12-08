from func import *
from collections import defaultdict
from itertools import accumulate


inp = read_input("input")
#  inp = read_input("test_input")

def parse_input(data:list)->dict:
    sizes:defaultdict=defaultdict(int)
    for line in data:
        match line.split():
            case "$", "cd", "/"  : path=["/"]
            case "$", "cd", ".." : path.pop()
            case "$", "cd", f    : path.append(f+"/")
            case "$", "ls"       : pass
            case  "dir",_        : pass
            case val, _:
                for p in accumulate(path):
                    sizes[p] += int(val)
    return sizes

sizes= parse_input(inp)
tot= sum(v for v in sizes.values() if v<=100_000)
print(tot)
