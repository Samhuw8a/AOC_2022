from func import *

inp = read_input("test_input")[0]
inp = read_input("input")[0]

def first_pack(s:str)->int:
    for i in range(14,len(s)):
        if len(set(s[i-14:i]))==14 :
            return i
    return 0

print(first_pack(inp))
print(first_pack("bvwbjplbgvbhsrlpgdmjqwftvncz"))
