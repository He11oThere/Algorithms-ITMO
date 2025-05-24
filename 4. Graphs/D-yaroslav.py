import sys
import heapq

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    d = int(data[1])
    a = [0] * (n)
    ind = 2

    for i in range(1, n-1):
        a[i] = int(data[ind])

        ind += 1

    coords = []

    for _ in range(n):
        x = int(data[ind])
        y = int(data[ind+1])
        coords.append((x, y))

        ind += 2

    return n, d, a, coords

def can_reach(n, d, a, coords, init_fuel):
    best = [-1] * n
    best[0] = init_fuel
    pq = [(-init_fuel, 0)]

    while pq:
        f, u = heapq.heappop(pq)
        f = -f

        if u == n-1:
            return True

        if f < best[u]:
            continue

        ux, uy = coords[u]
        for v in range(n):
            if v == u:
                continue

            vx, vy = coords[v]
            cost = d * (abs(ux - vx) + abs(uy - vy))

            if f >= cost:

                nf = f - cost + a[v]

                if nf > best[v]:
                    best[v] = nf
                    heapq.heappush(pq, (-nf, v))

    return False

def start():
    n, d, a, coords = read_data()
    left, right = 0, 10**8
    ans = right

    while left <= right:

        mid = (left + right) // 2

        if can_reach(n, d, a, coords, mid):
            ans = mid
            right = mid-1
        else:
            left = mid+1

    print(ans)

start()
