import sys

def read_data():
    return sys.stdin.readline().strip()

def min_replacements(s):
    n = len(s)

    if n % 2 != 0:
        return None

    stack = []

    pairs = {'<':'>', '{':'}', '[':']', '(':')'}

    opens = set(pairs.keys())

    closes = set(pairs.values())

    inv = {v:k for k,v in pairs.items()}

    count = 0
    for ch in s:

        if ch in opens:
            stack.append(ch)

        elif ch in closes:
            if not stack:
                return None

            o = stack.pop()
            if pairs[o] != ch:
                count += 1

        else:
            return None

    if stack:
        return None

    return count

def start():
    s = read_data()
    res = min_replacements(s)

    if res is None:
        print("Impossible")
    else:
        print(res)

start()
