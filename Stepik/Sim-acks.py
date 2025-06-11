import sys
from collections import deque

def read_data():
    data = sys.stdin.read().split()
    S = int(data[0])
    n = int(data[1])
    i = 2
    paks = []
    for _ in range(n):
        t = int(data[i]); p = int(data[i + 1])
        paks.append((t, p))
        i += 2

    return S, paks


def process_packets(S, paks):
    q = deque()
    result = []
    for t, p in paks:

        while q and q[0] <= t:
            q.popleft()

        if len(q) >= S:
            result.append(-1)
        else:
            start_time = t if not q else q[-1]
            finish_time = start_time + p
            q.append(finish_time)
            result.append(start_time)

    return result


S, packets = read_data()
ans = process_packets(S, packets)
for x in ans:
    print(x)
