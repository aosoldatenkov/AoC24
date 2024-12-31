import time

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]    

def minpath(w, h, walls, x, y):
    out = {(x, y): 0}
    new = [(x, y)]
    while new:
        p = new.pop(0)
        for d in dirs:
            q = (p[0] + d[0], p[1] + d[1])
            if q not in out and 0 <= q[0] < w and 0 <= q[1] < h and q not in walls:
                out[q] = out[p] + 1
                new.append(q)
    return out

def solve1(inp, d, n):
    walls = [tuple(int(a) for a in l.split(',')) for l in inp.splitlines()]
    dist = minpath(d, d, walls[:n], 0, 0)
    return dist[d - 1, d - 1]
    
def solve2(inp, d):
    walls = [tuple(int(a) for a in l.split(',')) for l in inp.splitlines()]
    head, tail = 0, len(walls) - 1
    while head < tail:
        mid = (head + tail) // 2
        dist = minpath(d, d, walls[:mid + 1], 0, 0)
        if (d - 1, d - 1) not in dist:
            tail = mid
        else:
            head = mid + 1
    return walls[head]

def run():
    if test:
        t1 = time.time()
        assert (r1 := solve1(test, 7, 12)) == 22
        t2 = time.time()
        assert (r2 := solve2(test, 7)) == (6, 1)
        t3 = time.time()
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        assert (r1 := solve1(inpt, 71, 1024)) == 340
        t2 = time.time()
        assert (r2 := solve2(inpt, 71)) == (34, 32)
        t3 = time.time()
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()
