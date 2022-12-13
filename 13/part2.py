from func import *
inp = read_input("input",sep="\n\n")
#  inp = read_input("test_input",sep="\n\n")
inp = mapl(lambda x : x.split("\n"),inp)
del inp[-1][-1]
inp = mapl(eval, flatten(inp))
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

def divider_index(packets, target):
    return sum(compair(p, target) <= 0 for p in packets)

two, six = [[2]], [[6]]
inp += [two, six]
tot= divider_index(inp, two) * divider_index(inp, six)
print(tot)
