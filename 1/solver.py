import itertools as it
import operator
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    nums = [int(x) for x in re.findall(r'\d+', inp)]
    A, B = sorted(nums[0::2]), sorted(nums[1::2])
    count = sum(abs(a - b) for a, b in zip(A, B))
    return count

def solve2(inp):
    nums = [int(x) for x in re.findall(r'\d+', inp)]
    A, B = nums[0::2], nums[1::2]
    count = sum(x * B.count(x) for x in A)
    return count

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
