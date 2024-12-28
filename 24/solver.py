import itertools as it
import re
import math
import random
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    b1, b2 = inp.split('\n\n')
    wires = {l.split(': ')[0]: int(l.split(': ')[1]) for l in b1.splitlines()}
    b2 = [tuple(l.split(' -> ')) for l in b2.splitlines()]
    gates = [(*op.split(), out) for op, out in b2]
    names = [w for w in wires]
    znames = sorted([g[3] for g in gates if g[3][0] == 'z'])
    while any(z not in wires for z in znames):
        for g in gates:
            if g[0] not in wires or g[2] not in wires:
                continue
            if g[1] == 'AND':
                wires[g[3]] = wires[g[0]] & wires[g[2]]
            elif g[1] == 'OR':
                wires[g[3]] = wires[g[0]] | wires[g[2]]
            else:
                wires[g[3]] = wires[g[0]] ^ wires[g[2]]
    out = 0
    for z in znames[::-1]:
        print(z, wires[z])
        out = (out << 1) + wires[z]
    return out

def trackback(scheme, name):
    if name not in scheme:
        return set()
    return {name, scheme[name][0], scheme[name][2]} | trackback(scheme, scheme[name][0]) | trackback(scheme, scheme[name][2])

def compute(scheme, inp):
    wires = dict(inp)
    outputs = set(scheme.keys())
    known = {w for w in wires}
    op = True
    while len(outputs) > 0 and op:
        op = False
        for s in scheme:
            g = scheme[s]
            if s in known or g[0] not in known or g[2] not in known:
                continue
            op = True
            if g[1] == 'AND':
                wires[s] = wires[g[0]] & wires[g[2]]
            elif g[1] == 'OR':
                wires[s] = wires[g[0]] | wires[g[2]]
            else:
                wires[s] = wires[g[0]] ^ wires[g[2]]
            outputs.remove(s)
            known.add(s)    
    return wires

def check(wires, result):
    return [n for n in result if n[0] == 'z' and (n not in wires or result[n] != wires[n])]

def exchange(scheme, inp, result):
    outputs = set(scheme.keys())
    faults = []
    #L = len(outputs)
    #print('Totat:', L * (L - 1) // 2)
    count = 0
    o1 = 'z31'
    for o2 in outputs:
        #print(count, end='\r')
        s = scheme.copy()
        s[o1], s[o2] = scheme[o2], scheme[o1]
        wires = compute(s, inp)
        faults.append((check(wires, result), o1, o2))
        #count += 1
    print(min(len(f[0]) for f in faults), max(len(f[0]) for f in faults))
    m = min(len(f[0]) for f in faults)
    for f in faults:
        if len(f[0]) == m:                
            print(f)
            s = scheme.copy()
            o1, o2 = f[1], f[2]
            s[o1], s[o2] = scheme[o2], scheme[o1]
            wires = compute(s, inp)
            for n in f[0]:
                print(n, wires[n], result[n])

def swap(scheme, pairs):
    s = scheme.copy()
    for a, b in pairs:
        s[a] = scheme[b]
        s[b] = scheme[a]
    return s

def test(scheme, r):
    wires = {}
    result = {}
    faults = set()
    for _ in range(r):
        X = random.randrange(2 ** 45)
        Y = random.randrange(2 ** 45)
        Z = X + Y
        for i in range(45):
            nameX = 'x0' + str(i) if i < 10 else 'x' + str(i)
            wires[nameX] = (X >> i) & 1
            nameY = 'y0' + str(i) if i < 10 else 'y' + str(i)
            wires[nameY] = (Y >> i) & 1
        for i in range(46):
            nameZ = 'z0' + str(i) if i < 10 else 'z' + str(i)
            result[nameZ] = (Z >> i) & 1
        w = compute(scheme, wires)
        faults.update(check(w, result))
    #print(sorted(g for g in faults))
    return faults

def try_swaps(scheme):
    s = swap(scheme, [('z11', 'z12'), ('z31', 'z32'), ('z15', 'z38'), ('vsd', 'fmk')])
    wires = {}
    result = {}
    for X, Y in it.product(range(2 ** 16, 2 ** 17), range(2 ** 16, 2 ** 17)):
        print(X, Y, end='\r')
        Z = X + Y
        for i in range(45):
            nameX = 'x0' + str(i) if i < 10 else 'x' + str(i)
            wires[nameX] = (X >> i) & 1
            nameY = 'y0' + str(i) if i < 10 else 'y' + str(i)
            wires[nameY] = (Y >> i) & 1
        for i in range(46):
            nameZ = 'z0' + str(i) if i < 10 else 'z' + str(i)
            result[nameZ] = (Z >> i) & 1
        w = compute(s, wires)
        if check(w, result) != []:
            print(X, Y, check(w, result))
            break
    

def solve2(inp):
    b1, b2 = inp.split('\n\n')
    wires = {l.split(': ')[0]: int(l.split(': ')[1]) for l in b1.splitlines()}
    X = Y = 0
    for i in range(45):
        nameX = 'x0' + str(i) if i < 10 else 'x' + str(i)
        X += wires[nameX] << i
        nameY = 'y0' + str(i) if i < 10 else 'y' + str(i)
        Y += wires[nameY] << i
    Z = X + Y
    
    b2 = [tuple(l.split(' -> ')) for l in b2.splitlines()]
    gates = [(*op.split(), out) for op, out in b2]
    names = [w for w in wires]
    znames = sorted([g[3] for g in gates if g[3][0] == 'z'])
    scheme = dict()
    for g in gates:
        scheme[g[3]] = (g[0], g[1], g[2])
    outputs = set(scheme.keys())
        
    result = {}
    for i in range(46):
        nameZ = 'z0' + str(i) if i < 10 else 'z' + str(i)
        result[nameZ] = (Z >> i) & 1
    #    print(nameZ, sorted(n for n in trackback(scheme, nameZ) if n[0] in ['x', 'y']))

    print(','.join(sorted(['z11', 'rpv', 'ctg', 'rpb', 'dmh', 'z31', 'z38', 'dvq'])))
    
    s = swap(scheme, [('z11', 'rpv'), ('ctg', 'rpb'), ('dmh', 'z31'), ('z38', 'dvq')])
    w = compute(s, wires)
    print(check(w, result))
    print(sorted(test(s, 30000)))

    scheme = swap(scheme, [('z11', 'rpv'), ('ctg', 'rpb'), ('dmh', 'z31')])
    good = set()
    for out in scheme.keys():
        dep_x = [n for n in trackback(scheme, out) if n[0] == 'x']
        dep_y = [n for n in trackback(scheme, out) if n[0] == 'y']
        if all(x <= 'x45' for x in dep_x) and all(y <= 'y45' for y in dep_y):
            good.add(out)
    print(good - trackback(scheme, 'z45'))
    print(trackback(scheme, 'z45') - trackback(scheme, 'z44'))

    potent = [x for x in good - trackback(scheme, 'z44') if x[0] != 'z']
    potent.append('z45')
    print(potent)
    m = 46
    for perm in it.permutations(potent, 2):
        swaps = [(a, b) for a, b in it.batched(perm, 2)]
        print(swaps, end='\r')
        s = swap(scheme, swaps)
        faults = test(s, 1000)
        if 'z45' not in faults:
            print('\n clear!', len(faults))

    #w = compute(scheme, wires)
    #print(check(w, result))

    #exchange(scheme, wires, result)

    return 0#sorted(check(wires, result))

random.seed()    
print(solve2(inpt))
#results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
