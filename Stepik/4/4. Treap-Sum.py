import sys
import random
sys.setrecursionlimit(1<<25)

MOD = 10**9 + 1

def get_sum(node): return node.sum if node else 0

def update(node):
    if node: node.sum = get_sum(node.left) + node.key + get_sum(node.right)

class TreapNode:
    __slots__ = ('key','prio','left','right','sum')
    def __init__(self, key):
        self.key = key
        self.prio = random.randrange(1<<30)
        self.left = None
        self.right = None
        self.sum = key

def split(node, key):
    if not node: return (None, None)

    if key <= node.key:
        l, node.left = split(node.left, key)
        update(node)
        return (l, node)
    else:
        node.right, r = split(node.right, key)
        update(node)
        return (node, r)

def merge(left, right):
    if not left or not right: return left or right

    if left.prio < right.prio:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

def insert(node, key):
    node = erase(node, key)
    new = TreapNode(key)
    l, r = split(node, key)

    return merge(merge(l, new), r)

def erase(node, key):
    if not node: return None

    if node.key == key:
        return merge(node.left, node.right)
    if key < node.key:
        node.left = erase(node.left, key)
    else:
        node.right = erase(node.right, key)
    update(node)

    return node

def find(node, key):
    while node:
        if node.key == key: return True
        node = node.left if key < node.key else node.right

    return False

def range_sum(node, l, r):
    a, bc = split(node, l)
    b, c = split(bc, r+1)
    res = get_sum(b)
    node = merge(a, merge(b, c))

    return node, res

def start():
    input = sys.stdin.readline
    n = int(input())
    root = None
    last = 0
    out = []
    for _ in range(n):
        parts = input().split()
        cmd = parts[0]
        if cmd == '+':
            x = (int(parts[1]) + last) % MOD
            root = insert(root, x)
        elif cmd == '-':
            x = (int(parts[1]) + last) % MOD
            root = erase(root, x)
        elif cmd == '?':
            x = (int(parts[1]) + last) % MOD
            out.append('Found' if find(root, x) else 'Not found')
        else:
            l = (int(parts[1]) + last) % MOD
            r = (int(parts[2]) + last) % MOD
            if l > r: l, r = r, l
            root, last = range_sum(root, l, r)
            out.append(str(last))
    print('\n'.join(out))

start()
