import re

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    nums = re.findall(r"mul\((\d+),(\d+)\)", inp)
    return sum(int(a) * int(b) for a, b in nums)

def solve2(inp):
    blocks = [re.split(r"don\'t\(\)", x)[0] for x in re.split(r"do\(\)", inp)]
    return sum(solve1(b) for b in blocks)

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
