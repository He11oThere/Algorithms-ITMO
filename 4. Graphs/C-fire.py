from collections import deque

def read_data():
    data = open('input.txt').read().split()

    n = int(data[0])
    m = int(data[1])
    k = int(data[2])

    sources = []
    i = 3

    for _ in range(k):
        x = int(data[i]) - 1
        y = int(data[i+1]) - 1
        sources.append((x, y))

        i += 2

    return n, m, sources

def bfs_dist(n, m, sources):
    visited = bytearray(n * m)
    q = deque()

    for x, y in sources:
        i = x * m + y
        visited[i] = 1
        q.append(i)

    last_i = None
    moves = (-1, 1, 0, 0), (0, 0, -1, 1)

    while q:
        i = q.popleft()
        last_i = i
        x, y = divmod(i, m)

        for dx, dy in zip(*moves):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                ni = nx * m + ny

                if not visited[ni]:
                    visited[ni] = 1
                    q.append(ni)

    return divmod(last_i, m)


def start():
    n, m, sources = read_data()
    x, y = bfs_dist(n, m, sources)

    with open('output.txt', 'w') as f:
        f.write(f"{x+1} {y+1}")

    print(f'{x+1} {y+1}')

start() # 3 тесткейс снова не совпадает
