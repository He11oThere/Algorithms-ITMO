import sys
from itertools import permutations

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    k = int(data[1])
    nums = data[2:2+n]

    return n, k, nums

def apply_perm(s, perm):
    res = []
    for i in perm:
        res.append(s[i])

    return "".join(res)

def solve(k, nums):
    best_diff = 10**18
    i_s = list(range(k))

    for perm in permutations(i_s):
        vals = []

        for s in nums:
            ps = apply_perm(s, perm)
            vals.append(int(ps))

        diff = max(vals) - min(vals)

        if diff < best_diff:
            best_diff = diff

    print(best_diff)

def start():
    n, k, nums = read_data()
    solve(k, nums)


start()

