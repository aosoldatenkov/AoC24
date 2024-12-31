with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def check(nums):
    difs = [nums[i] - nums[i - 1] for i in range(1, len(nums))]
    if (all(d > 0 for d in difs) or all(d < 0 for d in difs)) and all(abs(d) < 4 for d in difs):
        return True
    return False

def solve1(inp):
    reports = inp.splitlines()
    safe = 0
    for r in reports:
        nums = [int(x) for x in r.split()]
        safe += 1 if check(nums) else 0
    return safe

def solve2(inp):
    reports = inp.splitlines()
    safe = 0
    for r in reports:
        nums = [int(x) for x in r.split()]
        if check(nums):
            safe += 1
        else:
            for i in range(len(nums)):
                nnums = nums[:i] + nums[i + 1:]
                if check(nnums):
                    safe += 1
                    break
    return safe

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
