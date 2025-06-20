import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    i = 1
    q = []
    for _ in range(n):
        cmd = data[i]
        key = data[i+1]
        i += 2
        if cmd == 'add':
            name = data[i]
            i += 1
            q.append((cmd, key, name))
        else:
            q.append((cmd, key, None))

    return q

def process(q):
    book = {}
    out = []
    for cmd, key, name in q:
        if cmd == 'add':
            book[key] = name
        elif cmd == 'del':
            if key in book:
                del book[key]
        else:
            out.append(book.get(key, 'not found'))

    return out

queries = read_data()
answers = process(queries)
print("\n".join(answers))
