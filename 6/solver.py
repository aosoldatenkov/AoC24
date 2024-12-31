import itertools as it
import time

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

def walk(inp):
    dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for y, l in enumerate(inp):
        if '^' in l:
            pos = (l.index('^'), y)
            break
    marked = {(pos, (0, -1))}
    for d in it.cycle(dirs):
        for i in it.count():
            x, y = pos[0] + d[0], pos[1] + d[1]
            if x < 0 or x >= len(inp[0]) or y < 0 or y >= len(inp):
                positions = {p for (p, v) in marked}
                return (positions, 0)
            if ((x, y), d) in marked:
                positions = {p for (p, v) in marked}
                return (positions, 1)
            if inp[y][x] == '#':
                break
            else:
                pos = (x, y)
                marked.add((pos, d))
    return None

def solve1(inp):
    inp = [list(l) for l in inp.splitlines()]
    return len(walk(inp)[0])

def solve2(inp):
    inp = [list(l) for l in inp.splitlines()]
    path = walk(inp)[0]
    count = 0
    for x, y in path:
        if inp[y][x] != '.':
            continue
        inp[y][x] = '#'
        if walk(inp)[1] == 1:
            count += 1
        inp[y][x] = '.'
    return count

def run():
    if test:
        t1 = time.time()
        r1 = solve1(test)
        t2 = time.time()
        r2 = solve2(test)
        t3 = time.time()
        assert r1 == 41, r2 == 6
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        r1 = solve1(inpt)
        t2 = time.time()
        r2 = solve2(inpt)
        t3 = time.time()
        assert r1 == 4559, r2 == 1604
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()

