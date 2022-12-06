from func import *

inp = read_input("input")[0]
#  inp = read_input("test_input")[0]
#  print(inp)

#  def first_pack(s:str)->int:
#      vis:list =[]
#      for i,c in enumerate(s):
#          if len(list(set(vis)))==4 and c not in vis:
#              print(i)
#              return(i)
#
#          if len(vis)==5:
#              del vis[0]
#          vis.append(c)
#      return 0

def first_pack(s:str)->int:
    for i in range(4,len(s)-1):
        test=s[i-4:i]
        marker = s[i+1]
        if len(list(set(test)))==4 and marker not in test:
            return i
    return 0


print(first_pack(inp))
