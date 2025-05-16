import sys

def get_weight(points):
    return points[1]

def get_x(points):
    return points[0]

def pick_lowest_weight_points(points, n):
    points_sorted = sorted(points, key=get_weight)
    return points_sorted[:2 * n]

def make_pairs(chosen, n):
    by_x = sorted(chosen, key=get_x)
    total = len(by_x)
    res = []
    for i in range(n):
        l = by_x[i][2]
        r = by_x[total-1-i][2]
        res.append((l, r))
    return res

def process(n, points):
    chosen = pick_lowest_weight_points(points, n)
    s = 0
    for point in chosen:
        s += get_weight(point)
    print(s)
    for l, r in make_pairs(chosen, n):
        print(l, r)

def tests(data):
    t = int(data[0])
    idx = 1
    tests = []

    for _ in range(t):
        while idx < len(data) and not data[idx].isdigit():
            idx += 1

        n = int(data[idx]); m = int(data[idx + 1]); idx += 2
        points = []

        for i in range(m):
            x = int(data[idx]); w = int(data[idx + 1])
            points.append((x, w, i + 1))
            idx += 2

        tests.append((n, m, points))

    return tests

def start():
    data = sys.stdin.read().split()
    for n, m, points in tests(data):
        process(n, points)

start()
