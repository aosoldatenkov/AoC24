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
    dirs = {'>': (1, 0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
    blocks = inp.split('\n\n')
    house = [[a for a in l] for l in blocks[0].splitlines()]
    moves = blocks[1].rstrip()
    w = len(house[0])
    h = len(house)
    y = min(i for i in range(h) if '@' in house[i])
    x = house[y].index('@')
    for m in moves:
        if m not in dirs:
            continue
        d = dirs[m]
        line = [house[y + d[1] * i][x + d[0] * i] for i in range(max(w, h)) if 0 <= y + d[1] * i < h and 0 <= x + d[0] * i < w]
        j = line.index('#')
        if '.' in line[:j]:
            j = line.index('.')
            new_line = ['.']
            new_line.extend(line[:j])
            #print(new_line)
            for i in range(j + 1):
                house[y + d[1] * i][x + d[0] * i] = new_line[i]
            x, y = x + d[0], y + d[1]
    count = sum(100 * y + x for x, y in it.product(range(w), range(h)) if house[y][x] == 'O')
#    for l in house:
#        print(''.join(l))
    return count

def move(house, x, y, d):
    match house[y + d[1]][x + d[0]]:
        case '.': 
            return {(x, y)}
        case '#':
            return set()
        case '[':
            m1 = move(house, x + d[0], y + d[1], d)
            m2 = move(house, x + d[0] + 1, y + d[1], d) if d[1] != 0 else m1
            return m1 | m2 | {(x, y)} if m1 != set() and m2 != set() else set()
        case ']':
            m1 = move(house, x + d[0], y + d[1], d)
            m2 = move(house, x + d[0] - 1, y + d[1], d) if d[1] != 0 else m1
            return m1 | m2 | {(x, y)} if m1 != set() and m2 != set() else set()

def solve2(inp):
    dirs = {'>': (1, 0), '^': (0, -1), '<': (-1, 0), 'v': (0, 1)}
    ext = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    b1, b2 = inp.split('\n\n')
    house = [list(''.join(ext[a] for a in l)) for l in b1.splitlines()]
    moves = b2.rstrip()
    w = len(house[0])
    h = len(house)
    y = min(i for i in range(h) if '@' in house[i])
    x = house[y].index('@')
    for m in moves:
        #for l in house:
        #    print(''.join(a for a in l))

        if m not in dirs:
            continue
        repl = move(house, x, y, dirs[m])
        #print(repl)
        if len(repl) == 0:
            continue
        new_house = [[a for a in l] for l in house]
        for a, b in repl:
            new_house[b][a] = '.'
        for a, b in repl:
            new_house[b + dirs[m][1]][a + dirs[m][0]] = house[b][a]
        new_house[y][x] = '.'
        new_house[y + dirs[m][1]][x + dirs[m][0]] = '@'
        house = [[a for a in l] for l in new_house]
        x, y = x + dirs[m][0], y + dirs[m][1]
#    for l in house:
#        print(''.join(a for a in l))
    return sum(100 * y + x for x, y in it.product(range(w), range(h)) if house[y][x] == '[')   

print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
