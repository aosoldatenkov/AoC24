import itertools as it
import re
import math
from functools import cache

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def tokens(n):
    det = n[0] * n[3] - n[1] * n[2]
    if det != 0:
        a = n[4] * n[3] - n[5] * n[2]
        b = n[5] * n[0] - n[4] * n[1]
        if a % det == 0 and b % det == 0:
            return 3 * (a // det) + (b // det)
        return 0
    print("Degenerate!!!")
    return 0

def solve1(inp):
    blocks = inp.split('\n\n')
    count = 0
    for b in blocks:
        nums = [int(n) for n in re.findall(r'\d+', b)]
        count += tokens(nums)
    return count

def solve2(inp):
    blocks = inp.split('\n\n')
    count = 0
    for b in blocks:
        nums = [int(n) for n in re.findall(r'\d+', b)]
        nums[4] += 10000000000000
        nums[5] += 10000000000000
        count += tokens(nums)
    return count

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
