import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def walk(inp):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for y, l in enumerate(inp):
        if '^' in l:
            pos = [l.index('^'), y]
            break
    marked = {(tuple(pos), (0, -1))}
    for d in it.cycle(dirs):
        for i in it.count():
            x, y = pos[0] + d[0], pos[1] + d[1]
            if x < 0 or x >= len(inp[0]) or y < 0 or y >= len(inp):
                positions = {p for (p, v) in marked}
                return (len(positions), 0)
            if ((x, y), d) in marked:
                positions = {p for (p, v) in marked}
                return (len(positions), 1)
            if inp[y][x] == '#':
                break
            else:
                pos[0], pos[1] = x, y
                marked.add(((pos[0], pos[1]), d))
    return 0

def solve1(inp):
    inp = [list(l) for l in inp.splitlines()]
    return walk(inp)[0]

def solve2(inp):
    inp = [list(l) for l in inp.splitlines()]
    count = 0
    for y in range(len(inp)):
        print(y, ' of ', len(inp) - 1)
        for x in range(len(inp[0])):
            if inp[y][x] != '.':
                continue
            inp[y][x] = '#'
            if walk(inp)[1] == 1:
                count += 1
            inp[y][x] = '.'
    return count

print(solve2(inpt))


#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
