import sys

def bin_search(lower_bound, upper_bound, pr):
    while True:
        if lower_bound == upper_bound:
            return lower_bound
        mid = (lower_bound + upper_bound) // 2

        if mid == lower_bound:
            return upper_bound if pr(upper_bound) else lower_bound

        if pr(mid):
            lower_bound = mid
        else: upper_bound = mid - 1


def check(n, k, m, arr):
    trans = [1 if x >= m else -1 for x in arr]

    pref = [0]
    for i in trans:
        pref.append(pref[-1] + i)

    min_pref = [0]
    for i in pref[1:]:
        min_pref.append(min(min_pref[-1], i))

    for i in range(k, n+1):
        if pref[i] - min_pref[i-k] > 0:
            return True
    return False

def max_median(n, k, arr):
    return bin_search(1, n, lambda m: check(n, k, m, arr))

inp = sys.stdin.read().strip().split()
n = int(inp[0])
k = int(inp[1])
arr = list(map(int, inp[2:2+n]))
r = max_median(n, k, arr)
print(r)
