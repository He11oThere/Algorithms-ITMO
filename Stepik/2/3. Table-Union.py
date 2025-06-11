import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    m = int(data[1])
    sizes = list(map(int, data[2:2+n]))
    i = 2 + n
    merges = []
    for _ in range(m):
        x = int(data[i])
        y = int(data[i + 1])
        merges.append((x-1, y-1))
        i += 2

    return n, sizes, merges

def process(n, sizes, merges):
    parent = list(range(n))
    comp_size = sizes[:]
    max_size = max(sizes)

    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]


    def union(u, v):
        nonlocal max_size
        ru = find(u)
        rv = find(v)

        if ru != rv:
            if comp_size[ru] < comp_size[rv]:
                ru, rv = rv, ru

            parent[rv] = ru
            comp_size[ru] += comp_size[rv]

            if comp_size[ru] > max_size:
                max_size = comp_size[ru]

        return max_size

    result = []
    for u, v in merges:
        result.append(str(union(u, v)))

    return result


n, sizes, merges = read_data()
ans = process(n, sizes, merges)
print("\n".join(ans))
