import sys
import heapq # для дейкстры нужна приорити ку, а в питоне таких структур нет. Этот модуль предоставляет её

def read_graph(data, idx):
    n = int(data[idx]); m = int(data[idx + 1])
    idx += 2
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        u = int(data[idx]); v = int(data[idx + 1]); w = int(data[idx + 2])
        idx += 3
        graph[u].append((v, w))
        graph[v].append((u, w))

    return n, graph, idx

def dij(n, graph):
    dist = [10**30] * (n+1)
    prev = [-1] * (n+1)
    dist[1] = 0
    heap = [(0, 1)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue

        for (v, w) in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(heap, (nd, v))

    return dist, prev

def do_path(prev, n):
    if prev[n] == -1 and n != 1:
        return []

    path = []
    cur = n
    while cur != -1:
        path.append(cur)
        cur = prev[cur]
    path.reverse()

    return path

def start():
    data = sys.stdin.read().split()
    n, graph, _ = read_graph(data, 0)
    dist, prev = dij(n, graph)
    path = do_path(prev, n)

    if not path:
        print(-1)

    else:
        print(' '.join(str(x) for x in path))

start()
