import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    nodes = []
    i = 1

    for _ in range(n):
        val = int(data[i])
        left = int(data[i+1])
        right = int(data[i+2])
        nodes.append((val, left, right))
        i += 3

    return n, nodes

def is_bst(nodes):
    if not nodes:
        return True

    stack = [(0, -10**18, 10**18)]

    while stack:
        u, low, high = stack.pop()
        if u == -1:
            continue
        val, left, right = nodes[u]
        if val < low or val >= high:
            return False
        stack.append((right, val, high))
        stack.append((left, low, val))

    return True

n, nodes = read_data()
print("CORRECT" if is_bst(nodes) else "INCORRECT")
