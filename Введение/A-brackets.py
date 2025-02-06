d = {}
def scan():
    t = int(input())
    for i in range(1, t+1):
        n = int(input())
        s = input().strip()
        d[i] = [n, s]

def move_brackets(string: str) -> int:
    l = len(string)
    b = 0
    for i in range(l):
        if string[i] == '(': b += 1
        elif string[i] == ')': b -= 1
