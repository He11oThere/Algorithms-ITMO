def scan():
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input().strip()
        print(moves(s))

def moves(string: str) -> int:
    b = 0
    k = 0
    for i in range(len(string)):
        if string[i] == '(': b += 1
        elif string[i] == ')': b -= 1
        if b < 0: k += 1; b = 0
    return k

scan()
