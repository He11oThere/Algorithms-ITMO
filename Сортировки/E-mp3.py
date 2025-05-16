import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    I = int(data[1]) * 8
    arr = list(map(int, data[2:2+n]))

    return n, I, arr


def compute_M(n, I):
    k = I // n

    if k >= 30:
        return n

    return 1 << k


def do_freq(arr):
    freq = {}
    for x in arr:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1

    return freq


def start():
    n, I, arr = read_data()
    freq = do_freq(arr)
    uniq = list(freq.keys())
    uniq.sort()
    total_uniq = len(uniq)
    M = compute_M(n, I)

    if total_uniq <= M:
        print(0)

        return

    k = [freq[x] for x in uniq]
    pref = [0] * (total_uniq + 1)
    for i in range(total_uniq):
        pref[i + 1] = pref[i] + k[i]


    best = 0
    for left in range(0, total_uniq - M + 1):
        right = left + M
        cov = pref[right] - pref[left]
        if cov > best:
            best = cov

    print(n - best)


start()

