import sys
from collections import deque

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))
    k = int(data[1+n])

    return n, arr, k


def sliding_maximum(n, arr, k):
    dq = deque()
    result = []
    for i in range(n):

        if dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)
        if i >= k - 1:
            result.append(str(arr[dq[0]]))

    return result


n, arr, k = read_data()
res = sliding_maximum(n, arr, k)
print(" ".join(res))
