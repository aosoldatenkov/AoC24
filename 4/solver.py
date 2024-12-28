import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def get(lines, x, y, w, h):
    return lines[y][x] if (0 <= x < w and 0 <= y < h) else '.'

def solve1(inp):
    lines = [list(x.rstrip()) for x in inp.splitlines()]
    height = len(lines)
    width = len(lines[0])
    words = []
    for x, y, dx, dy in it.product(range(width), range(height), [-1, 0, 1], [-1, 0, 1]):
        words.append(''.join([get(lines, x + i * dx, y + i * dy, width, height) for i in range(4)]))
    return words.count("XMAS")

def solve2(inp):
    lines = [list(x.rstrip()) for x in inp.splitlines()]
    height = len(lines)
    width = len(lines[0])
    words = []
    for x, y in it.product(range(1, width - 1), range(1, height - 1)):
        block = [lines[y + j][x + i] for i, j in it.product([-1, 0, 1], [-1, 0, 1])]
        words.append(''.join(block[::2]))
    return words.count("MMASS") + words.count("SMASM") + words.count("SSAMM") + words.count("MSAMS")

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
