import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    rounds = []
    i = 1

    for _ in range(n):
        name = data[i]
        score = int(data[i+1])
        rounds.append((name, score))

        i += 2

    return rounds

def final_scores(rounds):
    totals = {}

    for name, score in rounds:
        if name not in totals:
            totals[name] = 0

        totals[name] += score

    return totals

def max_score_players(totals):
    max_score = max(totals.values())
    players = set(name for name, score in totals.items() if score == max_score)

    return max_score, players

def winner(rounds, max_score, candidates):
    running = {}

    for name, score in rounds:
        if name not in running:
            running[name] = 0

        running[name] += score
        if name in candidates and running[name] >= max_score:
            return name

    return None

def start():
    rounds = read_data()
    totals = final_scores(rounds)
    max_score, candidates = max_score_players(totals)
    win = winner(rounds, max_score, candidates)

    print(win)

start()
