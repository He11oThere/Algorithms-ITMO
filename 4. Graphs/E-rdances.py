import sys

def read_data():
    data = sys.stdin.read().split()
    t = int(data[0])
    ind = 1
    tests = []

    for _ in range(t):
        n = int(data[ind])
        ind += 1
        a = [0]*(n+1)

        for i in range(1, n+1):
            a[i] = int(data[ind])
            ind += 1

        tests.append((n, a))

    return tests

def cyc(n, a):
    color = [0] * (n+1)
    depth = [0] * (n+1)
    Ck = 0
    C2 = 0

    for i in range(1, n+1):
        if color[i] != 0:
            continue

        u = i
        step = 1
        while color[u] == 0:
            color[u] = 1
            depth[u] = step
            step += 1
            u = a[u]

        if color[u] == 1:
            length = step - depth[u]
            if length == 2:
                C2 += 1
            else:
                Ck += 1

        v = i
        while color[v] == 1:
            color[v] = 2
            v = a[v]

    maxi = Ck + C2
    mini = Ck + (1 if C2 > 0 else 0)
    return mini, maxi

def start():
    tests = read_data()
    out = []

    for n, a in tests:
        mini, maxi = cyc(n, a)
        out.append(f"{mini} {maxi}")

    print("\n".join(out))

start()
