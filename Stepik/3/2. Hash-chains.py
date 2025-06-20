import sys

def read_data():
    data = sys.stdin.read().split()
    m = int(data[0])
    n = int(data[1])
    queries = []
    i = 2
    while i < len(data):
        cmd = data[i]
        if cmd == "check":
            queries.append((cmd, int(data[i+1])))
            i += 2
        else:
            queries.append((cmd, data[i+1]))
            i += 2

    return m, queries

def poly_hash(s, m, p=1_000_000_007, x=263):
    hash_val = 0
    for c in reversed(s):
        hash_val = (hash_val * x + ord(c)) % p

    return hash_val % m

def process_queries(m, queries):
    buckets = [[] for _ in range(m)]
    output = []

    for query in queries:
        cmd, arg = query

        if cmd == "add":
            h = poly_hash(arg, m)
            if arg not in buckets[h]:
                buckets[h].insert(0, arg)

        elif cmd == "del":
            h = poly_hash(arg, m)
            if arg in buckets[h]:
                buckets[h].remove(arg)

        elif cmd == "find":
            h = poly_hash(arg, m)
            output.append("yes" if arg in buckets[h] else "no")

        elif cmd == "check":
            output.append(" ".join(buckets[arg]))

    return output

m, queries = read_data()
result = process_queries(m, queries)
print("\n".join(result))
