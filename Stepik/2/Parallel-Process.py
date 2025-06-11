import sys
import heapq

def read_data():
    data = sys.stdin.read().split()
    num_workers = int(data[0])
    num_jobs = int(data[1])
    jobs = list(map(int, data[2:2+num_jobs]))

    return num_workers, jobs


def process(num_workers, jobs):
    heap = [(0, i) for i in range(num_workers)]
    heapq.heapify(heap)
    result = []
    for duration in jobs:
        finish, worker = heapq.heappop(heap)
        result.append((worker, finish))
        heapq.heappush(heap, (finish + duration, worker))

    return result


num_workers, jobs = read_data()
assignments = process(num_workers, jobs)
out = []
for w, start_time in assignments:
    out.append(f"{w} {start_time}")
print("\n".join(out))
