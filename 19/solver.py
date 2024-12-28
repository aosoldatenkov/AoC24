import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    b1, b2 = inp.split('\n\n')
    pat = b1.split(', ')
    s = '(' + '|'.join(pat) + ')+'
    p = re.compile(s)
    designs = b2.splitlines()
    return sum(1 for d in designs if p.fullmatch(d) != None)

@cache
def match(s, pat):
    return 1 if s == '' else sum(match(s[len(p):], pat) for p in pat if s[:len(p)] == p)
    
def solve2(inp):
    b1, b2 = inp.split('\n\n')
    pat = tuple(b1.split(', '))
    designs = b2.splitlines()
    return sum(match(d, pat) for d in designs)

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
