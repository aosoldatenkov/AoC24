import itertools as it
import re
import math

with open("test") as f_test, open("input") as f_inp:
    test = f_test.read()
    inpt = f_inp.read()

def results(t1, i1, t2, i2):
    print("Part I:\n  test:", t1, "\n  input:", i1, "\nPart II:\n  test:", t2, "\n  input:", i2)

def solve1(inp):
    dmap = [int(x) for x in inp.rstrip()]
    nfiles = len(dmap) // 2
    L = sum(dmap)
    front_id = 0
    back_id = nfiles
    front_pos = 0
    back_pos = len(dmap) - 1
    checksum = 0
    for i in range(L):
        if front_pos % 2 == 0:
            dmap[front_pos] -= 1
            #print(i, front_id)
            checksum += i * front_id
            if dmap[front_pos] <= 0:
                front_id += 1
                front_pos += 1
        else:
            dmap[back_pos] -= 1
            dmap[front_pos] -= 1
            #print(i, back_id)
            checksum += i * back_id
            if dmap[back_pos] <= 0:
                back_id -= 1
                back_pos -= 2
        while dmap[front_pos] <= 0:
            front_pos += 1
        if front_pos > back_pos:
            break
    return checksum

def solve2(inp):
    files = []
    spaces = []
    n = 0
    cur_id = 0
    for a, b in it.batched(inp.rstrip() + '0', 2):
        files.append([cur_id, n, n + int(a)])
        if b != '0':
            spaces.append([n + int(a), n + int(a) + int(b)])
        n += int(a) + int(b)
        cur_id += 1
    for m, f in enumerate(files[::-1]):
        for n, s in enumerate(spaces):
            if f[1] < s[0]:
                break
            if f[2] - f[1] <= s[1] - s[0]:
                l = f[2] - f[1]
                files[len(files) - m - 1][1] = s[0]
                files[len(files) - m - 1][2] = s[0] + l
                #print(files)
                spaces[n][0] = s[0] + l
                break
    checksum = 0
    for f in files:
        for i in range(f[1], f[2]):
            checksum += f[0] * i
    return checksum

results(solve1(test), solve1(inpt), solve2(test), solve2(inpt))
