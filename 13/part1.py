from func import *
inp = read_input("input",sep="\n\n")
#  inp = read_input("test_input",sep="\n\n")
inp = mapl(lambda x : x.split("\n"),inp)
del inp[-1][-1]
print(inp)

def compair(left, right)->int:
    match left, right:
        case int(), int(): return left - right
        case list(), list():
            for l, r in zip(left, right):
                if diff := compair(l, r):
                    return diff
            return len(left) - len(right)
        case int(), list():
            return compair([left], right)
        case list(), int():
            return compair(left, [right])
    return 0

tot= sum(i for i, (l, r) in enumerate(inp, 1)
               if compair(eval(l), eval(r)) < 0)
print(tot)
