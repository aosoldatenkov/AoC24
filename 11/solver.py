import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    stones = inp.split()
    for i in range(25):
        new_stones = []
        for s in stones:
            if s == '0':
                new_stones.append('1')
            elif len(s) % 2 == 0:
                left = str(int(s[:len(s) // 2]))
                right = str(int(s[len(s) // 2:]))
                new_stones.append(left)
                new_stones.append(right)
            else:
                new_stones.append(str(int(s) * 2024))
        stones = new_stones
    return len(stones)

@cache
def get_len(s, n):
    if n == 0:
        return 1
    if s == '0':
        return get_len('1', n - 1)
    elif len(s) % 2 == 0:
        left = str(int(s[:len(s) // 2]))
        right = str(int(s[len(s) // 2:]))
        return get_len(left, n - 1) + get_len(right, n - 1)
    else:
        return get_len(str(int(s) * 2024), n - 1)

def solve2(inp):
    stones = inp.split()
    n = 0
    for s in stones:
        n += get_len(s, 75)
    return n

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
