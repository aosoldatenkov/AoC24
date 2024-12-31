import itertools as it
import time

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]    

def minpath(space, x, y):
    out = {(x, y): 0}
    new = [(x, y)]
    while new:
        p = new.pop(0)
        for d in dirs:
            q = (p[0] + d[0], p[1] + d[1])
            if q not in out and q in space:
                out[q] = out[p] + 1
                new.append(q)
    return out

def readmap(inp):
    return {(x, y): v for y, l in enumerate(inp.splitlines()) for x, v in enumerate(l)}

def solve1(inp, t):
    w = readmap(inp)
    xs, ys = {(x, y) for x, y in w if w[x, y] == 'S'}.pop()
    space = {(x, y) for x, y in w if w[x, y] != '#'}
    base = minpath(space, xs, ys)
    count = 0
    for x, y in w:
        if w[x, y] != '#':
            continue
        for d1, d2 in it.combinations(dirs, 2):
            x1, y1 = x + d1[0], y + d1[1]
            x2, y2 = x + d2[0], y + d2[1]
            if (x1, y1) in base and (x2, y2) in base:
                a, b = base[x1, y1], base[x2, y2]
                if abs(b - a) - 2 >= t:
                    count += 1
    return count

def solve2(inp, t):
    w = readmap(inp)
    xs, ys = {(x, y) for x, y in w if w[x, y] == 'S'}.pop()
    space = {(x, y) for x, y in w if w[x, y] != '#'}
    base = minpath(space, xs, ys)
    path = {base[x, y]: (x, y) for x, y in base}
    count = 0
    for a, b in it.combinations(range(len(path)), 2):
        p, q = path[a], path[b]
        d = abs(p[0] - q[0]) + abs(p[1] - q[1])
        if d <= 20 and b - a - d >= t:
            count += 1
    return count

def run():
    if test:
        t1 = time.time()
        r1 = solve1(test, 64)
        t2 = time.time()
        r2 = solve2(test, 76)
        t3 = time.time()
        assert r1 == 1
        assert r2 == 3
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        r1 = solve1(inpt, 100)
        t2 = time.time()
        r2 = solve2(inpt, 100)
        t3 = time.time()
        assert r1 == 1507
        assert r2 == 1037936
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()
