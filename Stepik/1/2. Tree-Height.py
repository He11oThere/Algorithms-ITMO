import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    parents = list(map(int, data[1:1 + n]))

    return n, parents


def compute_height(n, parents):
    depth = [0] * n

    def get_depth(u):
        if depth[u]:
            return depth[u]

        p = parents[u]
        if p == -1:
            depth[u] = 1
        else:
            depth[u] = get_depth(p) + 1
        return depth[u]

    max_h = 0
    for i in range(n):
        h = get_depth(i)
        if h > max_h:
            max_h = h

    return max_h


n, parents = read_data()
h = compute_height(n, parents)
print(h)
