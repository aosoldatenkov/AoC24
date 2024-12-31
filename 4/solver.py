import itertools as it
import time

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def get(lines, x, y, w, h):
    return lines[y][x] if (0 <= x < w and 0 <= y < h) else '.'

def solve1(inp):
    lines = [list(x) for x in inp.splitlines()]
    height = len(lines)
    width = len(lines[0])
    words = []
    for x, y in it.product(range(width), range(height)):
        if lines[y][x] != 'X':
            continue
        for dx, dy in it.product([-1, 0, 1], [-1, 0, 1]):
            words.append(''.join([get(lines, x + i * dx, y + i * dy, width, height) for i in range(4)]))
    return words.count("XMAS")

def solve2(inp):
    lines = [list(x) for x in inp.splitlines()]
    height = len(lines)
    width = len(lines[0])
    words = []
    for x, y in it.product(range(1, width - 1), range(1, height - 1)):
        if lines[y][x] != 'A':
            continue
        block = [lines[y + j][x + i] for i, j in it.product([-1, 0, 1], [-1, 0, 1])]
        words.append(''.join(block[::2]))
    return words.count("MMASS") + words.count("SMASM") + words.count("SSAMM") + words.count("MSAMS")

def run():
    if test:
        t1 = time.time()
        assert (r1 := solve1(test)) == 18
        t2 = time.time()
        assert (r2 := solve2(test)) == 9
        t3 = time.time()
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        assert (r1 := solve1(inpt)) == 2551
        t2 = time.time()
        assert (r2 := solve2(inpt)) == 1985
        t3 = time.time()
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()

