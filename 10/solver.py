import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def walk(x, y, hmap):
    if hmap[y][x] == 9:
        return {(x, y)}
    dirs = [(a, b) for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + a < len(hmap[0]) and 0 <= y + b < len(hmap) and hmap[y + b][x + a] - hmap[y][x] == 1]
    tops = set()
    for a, b in dirs:
        tops = tops | walk(x + a, y + b, hmap)
    return tops
    
def solve1(inp):
    hmap = [[int(n) for n in l] for l in inp.splitlines()]
    routes = []
    for y, l in enumerate(hmap):
        routes.extend(len(walk(x, y, hmap)) for x, h in enumerate(l) if h == 0)
    return sum(routes)

def walk2(x, y, hmap):
    if hmap[y][x] == 9:
        return 1
    dirs = [(a, b) for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + a < len(hmap[0]) and 0 <= y + b < len(hmap) and hmap[y + b][x + a] - hmap[y][x] == 1]
    return sum(walk2(x + a, y + b, hmap) for a, b in dirs)

def solve2(inp):
    hmap = [[int(n) for n in l] for l in inp.splitlines()]
    n = 0
    for y, l in enumerate(hmap):
        n += sum(walk2(x, y, hmap) for x, h in enumerate(l) if h == 0)                
    return n

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
