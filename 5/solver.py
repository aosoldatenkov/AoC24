import itertools as it
import re

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    first, second = inp.split('\n\n')
    first = re.split(r'\W', first)
    second = second.splitlines()
    ordering = [(int(a), int(b)) for a, b in it.batched(first, 2)]
    updates = [[int(x) for x in l.split(',')] for l in second]
    mid = []
    for u in updates:
        correct = True
        for a, b in ordering:
            if a in u and b in u and u.index(a) > u.index(b):
                correct = False
                break
        if correct:
            mid.append(u[len(u) // 2])
    return sum(mid)

def make_correct(u, ordering):
    new_u = [u[0]]
    for i in range(1, len(u)):
        j = 0
        while j < len(new_u) and (u[i], new_u[j]) not in ordering:
            j += 1
        new_u.insert(j, u[i])
    return new_u
        
def solve2(inp):
    first, second = inp.split('\n\n')
    first = re.split(r'\W', first)
    second = second.splitlines()
    ordering = [(int(a), int(b)) for a, b in it.batched(first, 2)]
    updates = [[int(x) for x in l.split(',')] for l in second]
    mid = []
    for u in updates:
        correct = True
        for a, b in ordering:
            if a in u and b in u and u.index(a) > u.index(b):
                correct = False
                break
        if not correct:
            new_u = make_correct(u, ordering)
            mid.append(new_u[len(new_u) // 2])
    return sum(mid)

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
