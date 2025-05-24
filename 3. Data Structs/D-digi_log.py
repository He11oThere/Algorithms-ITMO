import sys
import math
import heapq

def read_data():
    data = sys.stdin.read().split()
    t = int(data[0])
    i = 1
    tests = []

    for _ in range(t):
        n = int(data[i])
        i += 1
        a = list(map(int, data[i:i + n]))
        i += n
        b = list(map(int, data[i:i + n]))
        i += n

        tests.append((a, b))

    return tests

def digit_count(x):
    if x < 10:
        return 1

    return int(math.log10(x)) + 1

def compute_ops(a, b):
    ha = [-x for x in a]
    hb = [-x for x in b]
    heapq.heapify(ha)
    heapq.heapify(hb)
    ops = 0

    while ha and hb:
        va = -ha[0]
        vb = -hb[0]

        if va == vb:
            heapq.heappop(ha)
            heapq.heappop(hb)
        elif va > vb:
            heapq.heappop(ha)
            heapq.heappush(ha, -digit_count(va))
            ops += 1
        else:
            heapq.heappop(hb)
            heapq.heappush(hb, -digit_count(vb))
            ops += 1

    return ops

def start():
    tests = read_data()
    results = []

    for a, b in tests:
        results.append(str(compute_ops(a, b)))

    print("\n".join(results))

start()
