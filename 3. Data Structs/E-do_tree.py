import sys
import bisect

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    a = list(map(int, data[1:1+n]))

    return n, a

def compute_parents(n, a):
    sorted_vals = []
    insert_time = {}
    parent = [0] * n

    for i, val in enumerate(a):

        if not sorted_vals:
            sorted_vals.append(val)
            insert_time[val] = i

            continue

        pos = bisect.bisect_left(sorted_vals, val)
        pred = sorted_vals[pos-1] if pos-1 >= 0 else None
        succ = sorted_vals[pos] if pos < len(sorted_vals) else None

        if pred is None:
            p = succ
        elif succ is None:
            p = pred
        else:
            if insert_time[pred] > insert_time[succ]:
                p = pred
            else:
                p = succ

        parent[i] = p
        sorted_vals.insert(pos, val)
        insert_time[val] = i

    return parent

def start():
    n, a = read_data()
    parent = compute_parents(n, a)

    print(" ".join(str(parent[i]) for i in range(1, n)))

start()
