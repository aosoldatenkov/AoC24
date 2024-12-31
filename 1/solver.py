import time, re

try: 
    with open("test") as f_test: test = f_test.read()
except: test = None
try:
    with open("input") as f_inp: inpt = f_inp.read()
except: inpt = None

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

def run():
    if test:
        t1 = time.time()
        r1 = solve1(test)
        t2 = time.time()
        r2 = solve2(test)
        t3 = time.time()
        assert r1 == 11, r2 == 31
        print("Test I:", r1, f'{t2 - t1:10.3f}s', "\nTest II:", r2, f'{t3 - t2:10.3f}s')
    if inpt:
        t1 = time.time()
        r1 = solve1(inpt)
        t2 = time.time()
        r2 = solve2(inpt)
        t3 = time.time()
        assert r1 == 1319616, r2 == 27267728
        print("Part I:", r1, f'{t2 - t1:10.3f}s', "\nPart II:", r2, f'{t3 - t2:10.3f}s')

run()
