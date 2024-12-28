import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def output(A, B, C, code):
    ptr = 0
    out = []
    while ptr < len(code) - 1:
        literal = code[ptr + 1]
        if literal < 4:
            combo = literal
        elif literal == 4:
            combo = A
        elif literal == 5:
            combo = B
        else:
            combo = C
        match code[ptr]:
            case 0:
                A = A >> combo
            case 1:
                B = B ^ literal
            case 2:
                B = combo % 8
            case 3:
                if A != 0:
                    ptr = literal
                    continue
            case 4:
                B = B ^ C
            case 5:
                out.append(combo % 8)
            case 6:
                B = A >> combo
            case 7:
                C = A >> combo
        ptr += 2
    return out

def solve1(inp):
    b1, b2 = inp.split('\n\n')
    A, B, C = tuple(map(int, re.findall(r'\d+', b1)))
    _, b2 = b2.split() 
    code = list(map(int, b2.split(',')))
    return ','.join(str(a) for a in output(A, B, C, code))

@cache
def log2(x):
    for i in it.count():
        if x >> i == 0:
            return i

def find_A(code, A, B, C, i0=0):
    Abase = {A: 0}
    while True:
        out = []
        for a0 in Abase:
            a1 = Abase[a0]
            a = (a1 << log2(a0)) + a0
            o = output(a, B, C, tuple(code))
            out.append((o, a))
            Abase[a0] += 1
        for o, a in out:
            if len(o) <= len(code[i0:]) and code[i0:len(o)] == o and a not in Abase:
                print(code, o, a)
                Abase[a] = 0
        #if code in [o[0] for o in out]:
        #    vals = sorted(o[1] for o in out if o[0] == code)
        #    print(vals)
        #    return min(vals)
    
def solve2(inp):
    b1, b2 = inp.split('\n\n')
    A, B, C = tuple(map(int, re.findall(r'\d+', b1)))
    _, b2 = b2.split() 
    code = list(map(int, b2.split(',')))
    print(find_A(code, 0, 0, 0, i0=0))
    return 0
    #A = 202597226523177
    #while output(A, B, C, code) != code:
    #    A -= 1
    #    if A % 10000 == 0:
    #        print(A, output(A, B, C, code))
    #return A

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
