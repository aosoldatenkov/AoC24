with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def connect(x, y, gmap):
    letter  = gmap[y][x]
    dirs = [(a, b) for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)] if 0 <= x + a < len(gmap[0]) and 0 <= y + b < len(gmap)]
    return [(x + a, y + b) for a, b in dirs if gmap[y + b][x + a] == letter]

def cluster(x, y, nbr, c):
    if (x, y) in c:
        return c
    c_new = c | {(x, y)}
    for a, b in nbr[(x, y)]:
        c_new = c_new | cluster(a, b, nbr, c_new)
    return c_new

def solve1(inp):
    inp = [[x for x in l] for l in inp.splitlines()]
    nbr = dict()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            nbr[(x, y)] = connect(x, y, inp)
    pts = set()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            pts.add((x, y))
    cls = []
    while len(pts) > 0:
        for x, y in pts:
            c = cluster(x, y, nbr, set())
            break
        pts = pts - c
        cls.append(c)
    count = 0
    for c in cls:
        per = 0
        for x, y in c:
            per += 4 - len(nbr[(x, y)])
        count += per * len(c)
    return count

def solve2(inp):
    inp = [[x for x in l] for l in inp.splitlines()]
    nbr = dict()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            nbr[(x, y)] = connect(x, y, inp)
    pts = set()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            pts.add((x, y))
    cls = []
    while len(pts) > 0:
        for x, y in pts:
            c = cluster(x, y, nbr, set())
            break
        pts = pts - c
        cls.append(c)
    count = 0
    for c in cls:
        per = 0
        for x, y in c:
            per += 4 - len(nbr[(x, y)])
        for y in range(-1, len(inp)):
            for x in range(-1, len(inp[0])):
                if (x, y) in c and (x + 1, y) in c and (x, y + 1) not in c and (x + 1, y + 1) not in c:
                    per -= 1
                if (x, y) not in c and (x + 1, y) not in c and (x, y + 1) in c and (x + 1, y + 1) in c:
                    per -= 1
                if (x, y) in c and (x, y + 1) in c and (x + 1, y) not in c and (x + 1, y + 1) not in c:
                    per -= 1
                if (x, y) not in c and (x, y + 1) not in c and (x + 1, y) in c and (x + 1, y + 1) in c:
                    per -= 1
        count += per * len(c)
    return count

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
