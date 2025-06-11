import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    arr = list(map(int, data[1:1+n]))

    return n, arr


def build_heap(n, arr):
    swaps = []

    def sift_down(i):
        while True:
            l = 2*i+1
            r = 2*i+2
            smallest = i

            if l < n and arr[l] < arr[smallest]:
                smallest = l

            if r < n and arr[r] < arr[smallest]:
                smallest = r

            if smallest != i:
                swaps.append((i, smallest))
                arr[i], arr[smallest] = arr[smallest], arr[i]
                i = smallest
            else:
                break

    for i in range(n//2 - 1, -1, -1):
        sift_down(i)

    return swaps


n, arr = read_data()
swaps = build_heap(n, arr)
print(len(swaps))
for i, j in swaps:
    print(i, j)
