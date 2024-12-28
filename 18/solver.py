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
    m = [['.' for x in range(71)] for y in range(71)]
    inp = inp.splitlines()
    for i in range(1024):
        x, y = map(int, inp[i].split(','))
        m[y][x] = '#'
    pos = {(0, 0): 0}
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    new = {(0, 0)}
    while len(new) > 0:
        x, y = new.pop()
        val = pos[(x, y)]
        for dx, dy in dirs:
            x1, y1 = x + dx, y + dy
            if x1 < 0 or x1 > 70 or y1 < 0 or y1 > 70:
                continue
            if m[y1][x1] == '.' and ((x1, y1) not in pos or pos[(x1, y1)] > val + 1):
                pos[(x1, y1)] = val + 1
                new.add((x1, y1))
    return pos[(70, 70)]
    
def solve2(inp):
    m = [['.' for x in range(71)] for y in range(71)]
    inp = inp.splitlines()
    for i in range(1024):
        x, y = map(int, inp[i].split(','))
        m[y][x] = '#'
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in range(1024, len(inp)):
        a, b = map(int, inp[i].split(','))
        m[b][a] = '#'
        pos = {(0, 0): 0}
        new = {(0, 0)}
        while len(new) > 0:
            x, y = new.pop()
            val = pos[(x, y)]
            for dx, dy in dirs:
                x1, y1 = x + dx, y + dy
                if x1 < 0 or x1 > 70 or y1 < 0 or y1 > 70:
                    continue
                if m[y1][x1] == '.' and ((x1, y1) not in pos or pos[(x1, y1)] > val + 1):
                    pos[(x1, y1)] = val + 1
                    new.add((x1, y1))
        if (70, 70) not in pos:
            return a, b
    return 0
    

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
