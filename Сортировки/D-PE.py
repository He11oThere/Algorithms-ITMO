import sys

def trans(n, target, curr):
    moves = []

    for i in range(n):
        j = i

        while j < n and curr[j] != target[i]:
            j += 1

        while j > i:
            curr[j], curr[j - 1] = curr[j - 1], curr[j]
            moves.append((j, j + 1))
            j -= 1

    return moves

def start():
    inp = sys.stdin.read().split()
    n = int(inp[0])
    targ = list(map(int, inp[1:n + 1]))
    curr = list(map(int, inp[n + 1:2 * n + 1]))
    moves = trans(n, targ, curr)
    print(len(moves))

    for move in moves:
        print(move[0], move[1])

start()

