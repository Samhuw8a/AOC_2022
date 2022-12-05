import re
from itertools import chain
from collections.abc import Callable
from typing import Union, Any

# Most of this is shamelessly stolen from Peter Norvig.

cat = ''.join
inf = float('inf')
flatten = chain.from_iterable


def mapl(f: Callable, iterable)-> list:
    """gibt die Listenform einer Map aus"""
    return list(map(f, iterable))

def mapt(f: Callable, iterable)-> tuple:
    return tuple(map(f, iterable))

def filterl(f: Callable, iterable)-> list:
    return list(filter(f, iterable))

def read_input(filename, datatype=str, sep:str ='\n')-> list:
    """Liest die Input Datei aus als 'datatype' und splitet auf den Seperator."""
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    with open(f"{filename}.txt") as f:
        contents = f.read().strip().split(sep)
        return mapl(datatype, contents)

def digits(line:str)->tuple :
    """Gibt alle Digits ein einem String an."""
    return mapt(int, line)

def integers(text:str, negative:bool=True)-> tuple:
    """Gibt alle Zahlen in einem String aus. Wenn negative False ist werden alle Zahlen positiv gemacht."""
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))

def count(iterable, pred=bool)-> int:
    """Zählt alle Zahlen zusammen die die 'pred' bevolgen."""
    return sum(1 for item in iterable if pred(item))

def first(iterable, default=None)-> Any:
    """Gibt das erste Element eines iterable an."""
    return next(iter(iterable), default)

def filter_first(iterable, func: Callable):
    return first(el for el in iterable if func(el))

def manhattan(a:tuple , b:tuple = (0, 0) ) -> int:
    """Manhattan Distanz zwischen zwei punkten a,b (Minecraft ähnlich)"""
    return sum(abs(p - q) for p, q in zip(a, b))

def sign(n:Union[int,float]):
    """Gibt das 'sign' einer Zahl an."""
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0

def line_print(lines: str):
    """Druckt alle Linien in 'lines' Formatiert aus"""
    for line in lines:
        print(cat(line))

def maxval(d:dict):
    """Gib das Grösste Value eine Dictionarys an."""
    return max(d.values())

def transpose(matrix:Union[list,tuple]):
    """'Dreht' eine Matrix um."""
    return list(zip(*matrix))

def bin2int(s:str):
    """Convertiert eine Binärzahl in eine Decimalzahl."""
    return int(s, 2)

if __name__ == "__main__":
    assert cat(["ab", "cd", "ef"]) == "abcdef"
    assert mapl(int, ["1", "2"]) == [1, 2]
    assert mapt(int, ["1", "2"]) == (1, 2)
    assert filterl(lambda x: x > 3, [1, 5, 2, 4, 3]) == [5, 4]
    assert digits("123") == (1, 2, 3)
    assert integers("23 -42 55") == (23, -42, 55)
    assert integers("23 -42 55", negative=False) == (23, 42, 55)
    assert count([3, -5, 10, -7, 33], lambda x: x > 0) == 3
    assert first([2, 4, 6, 8]) == 2
    assert filter_first([2, 7, 4, 6, 8], lambda x: x > 5) == 7
    assert manhattan((5, -3)) == 8
    assert manhattan((5, -3), (2, 7)) == 13
    assert maxval(dict(a=3, b=99, c=66)) == 99
    assert bin2int("0101") == 5
