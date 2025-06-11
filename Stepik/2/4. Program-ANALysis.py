import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    e = int(data[1])
    d = int(data[2])
    i = 3
    unions = []
    for _ in range(e):
        u = int(data[i])
        v = int(data[i+1])
        unions.append((u, v))
        i += 2
    checks = []
    for _ in range(d):
        u = int(data[i])
        v = int(data[i+1])
        checks.append((u, v))
        i += 2

    return n, unions, checks

def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(parent, x, y):
    rx = find(parent, x)
    ry = find(parent, y)

    if rx != ry:
        parent[ry] = rx

def start():
    n, unions, checks = read_data()
    parent = list(range(n+1))

    for u, v in unions:
        union(parent, u, v)

    for u, v in checks:
        if find(parent, u) == find(parent, v):
            print(0)
            return

    print(1)

start()
