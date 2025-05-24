import sys

def read_ints(data, idx):
    n = int(data[idx]); m = int(data[idx+1])

    return (n, m), idx+2

def read_grid(data, idx, n, m):
    grid = []

    for _ in range(n):
        row = list(map(int, data[idx:idx+m]))
        grid.append(row)
        idx += m

    return grid, idx

def dfs(start_i, start_j, n, m, grid, visited):
    stack = [(start_i, start_j)]
    visited[start_i][start_j] = True
    volume = 0

    while stack:
        i, j = stack.pop()
        volume += grid[i][j]

        ni, nj = i-1, j
        if ni >= 0 and not visited[ni][nj] and grid[ni][nj] > 0:
            visited[ni][nj] = True
            stack.append((ni, nj))

        ni, nj = i+1, j
        if ni < n and not visited[ni][nj] and grid[ni][nj] > 0:
            visited[ni][nj] = True
            stack.append((ni, nj))

        ni, nj = i, j-1
        if nj >= 0 and not visited[ni][nj] and grid[ni][nj] > 0:
            visited[ni][nj] = True
            stack.append((ni, nj))

        ni, nj = i, j+1
        if nj < m and not visited[ni][nj] and grid[ni][nj] > 0:
            visited[ni][nj] = True
            stack.append((ni, nj))

    return volume

def solve_one(n, m, grid):
    visited = [[False]*m for _ in range(n)]
    max_vol = 0

    for i in range(n):

        for j in range(m):

            if grid[i][j] > 0 and not visited[i][j]:

                vol = dfs(i, j, n, m, grid, visited)

                if vol > max_vol:
                    max_vol = vol

    return max_vol

def start():
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1

    for _ in range(t):
        (n, m), idx = read_ints(data, idx)
        grid, idx = read_grid(data, idx, n, m)
        result = solve_one(n, m, grid)
        print(result)

start()
