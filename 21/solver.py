import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

kp1 = {'7': (0, 0), '8': (1, 0), '9': (2, 0), '4': (0, 1), '5': (1, 1), '6': (2, 1), '1': (0, 2), '2': (1, 2), '3': (2, 2), '0': (1, 3), 'A': (2, 3)}
kp1i = {kp1[k]: k for k in kp1}
kp2 = {'^': (1, 0), 'A': (2, 0), '<': (0, 1), 'v': (1, 1), '>': (2, 1)}
kp2i = {kp2[k]: k for k in kp2}
dirs = {'^': (0, -1), '<': (-1, 0), 'v': (0, 1), '>': (1, 0)}
opdirs = {'^': 'v', '<': '>', 'v': '^', '>': '<'}

def all_paths(keys):
    ikeys = {keys[k]: k for k in keys}
    paths = {(v, v): (0, {''}) for v in keys}
    new = set(paths.keys())
    while len(new) > 0:
        p = new.pop()
        c0, c1 = keys[p[0]], keys[p[1]]
        for d in dirs:
            c = (c0[0] + dirs[d][0], c0[1] + dirs[d][1])
            if c not in ikeys:
                continue
            s = ikeys[c]
            pp = (s, p[1])
            if pp not in paths or paths[pp][0] > paths[p][0] + 1:
                paths[pp] = (paths[p][0] + 1, {opdirs[d] + t for t in paths[p][1]})
                new.add(pp)
            elif paths[pp][0] == paths[p][0] + 1:
                paths[pp] = (paths[p][0] + 1, paths[pp][1] | {opdirs[d] + t for t in paths[p][1]})
                new.add(pp)
        for d in dirs:
            c = (c1[0] + dirs[d][0], c1[1] + dirs[d][1])
            if c not in ikeys:
                continue
            s = ikeys[c]
            pp = (p[0], s)
            if pp not in paths or paths[pp][0] > paths[p][0] + 1:
                paths[pp] = (paths[p][0] + 1, {t + d for t in paths[p][1]})
                new.add(pp)
            elif paths[pp][0] == paths[p][0] + 1:
                paths[pp] = (paths[p][0] + 1, paths[pp][1] | {t + d for t in paths[p][1]})
                new.add(pp)
    return paths

all1 = all_paths(kp1)
all2 = all_paths(kp2)

def move(pos, k, mov):
    p = list(pos)
    if k == 0 and mov != 'A':
        x, y = kp1[pos[0]]
        dx, dy = dirs[mov]
        x, y = x + dx, y + dy
        if (x, y) in kp1i:
           p[0] = kp1i[(x, y)]
    if k > 0:
        if mov != 'A':
            x, y = kp2[pos[k]]
            dx, dy = dirs[mov]
            x, y = x + dx, y + dy
            if (x, y) in kp2i:
                p[k] = kp2i[(x, y)]
        else:
            return move(pos, k - 1, pos[k])
    return tuple(p)

def path(p1, p2, n, bound=None):
    if bound == None:
        bound = 6 * (4 ** n)
    p1, p2 = tuple(p1 + 'A' * n), tuple(p2 + 'A' * n)
    pos = {p1: 0}
    new = {p1}
    while len(new) > 0:
        p = new.pop()
        if pos[p] >= bound:
            continue
        for mov in kp2:
            pp = move(p, n, mov)
            if pp not in pos or pos[pp] > pos[p] + 1:
                pos[pp] = pos[p] + 1
                new.add(pp)
    return pos[p2]
    
def solve1(inp):
    complexity = 0
    for code in inp.splitlines():
        l = 0
        for a, b in it.pairwise('A' + code):
            l += path(a, b, 2) + 1
        complexity += l * int(code[:-1])
    return complexity
    
def execute(keys, s):
    out = ''
    pos = keys['A']
    ikeys= {keys[k]: k for k in keys}
    for x in s:
        if x == 'A':
            out += ikeys[pos]
            continue
        d = dirs[x]
        pos = (pos[0] + d[0], pos[1] + d[1])
    return out

def expand(allp, n, s, start='A'):
    if len(s) == 0:
        return ['']
    if n == 0:
        return [s]
    step = [a + 'A' + b for a, b in it.product(allp[(start, s[0])][1], expand(allp, 1, s[1:], start=s[0]))]
    out = []
    for ss in step:
        out.extend(expand(allp, n - 1, ss, start=start))
    return out

#print(solve2(inpt))

#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))

def optimize_keys(keys, depth):
    out = {}
    for p in keys:
        best = 2 ** 100
        for r in keys[p][1]:
            best = min(best, min(map(len, expand(keys, depth, r + 'A'))))
        l = set()
        for r in keys[p][1]:
            if min(map(len, expand(keys, depth, r + 'A'))) == best:
                l.add(r)
        out[p] = (keys[p][0], l)
    return out

all2min = optimize_keys(all2, 2)
all2min = optimize_keys(all2min, 4)

all1min = {}
for p in all1:
    best = 2 ** 100
    for r in all1[p][1]:
        best = min(best, min(map(len, expand(all2min, 4, r + 'A'))))
    l = set()
    for r in all1[p][1]:
        if min(map(len, expand(all2min, 4, r + 'A'))) == best:
            l.add(r)
    all1min[p] = (all1[p][0], l)

#print('\n'.join(str(i) for i in all1min.items()))

def findone(code, depth):
    s = code#''
    #for p in it.pairwise('A' + code):
    #    s = s + list(all1min[p][1])[0] + 'A'
    #print(s, len(s))
    for i in range(depth):
        t = ''
        for p in it.pairwise('A' + s):
            t = t + list(all2min[p][1])[0] + 'A'
        s = t
        #print(t, len(t))
    return s

def solve2(inp):
    table = {}
    for p in all2min.keys():
        s = list(all2min[p][1])[0] + 'A'
        for i in range(12):
            t = ''
            for q in it.pairwise('A' + s):
                t = t + list(all2min[q][1])[0] + 'A'
            s = t
        table[p] = len(s)
        print(p, end='\r')
    print(table)
    complexity = 0
    for code in inp.splitlines():
        print('Doing code', code)
        s = ''
        for p in it.pairwise('A' + code):
            s += list(all1min[p][1])[0] + 'A'
        #print(s)
        for i in range(12):
            t = ''
            for p in it.pairwise('A' + s):
                t = t + list(all2min[p][1])[0] + 'A'
            s = t
        #print(s, sum(table[p] for p in it.pairwise('A' + s)))
        complexity += sum(table[p] for p in it.pairwise('A' + s)) * int(code[:-1])
    return complexity

print(solve2(inpt))

#print(len(findone('v>', 13)))

#for l in test.splitlines():
#    print(len(findone(l, 12)))
#print(execute(kp2, '<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'))
#print(execute(kp2, '<AAv<AA>>^AvA^AvA^A<vAA>^A'))
