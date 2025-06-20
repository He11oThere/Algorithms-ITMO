import sys
import random

sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

class Node:
    __slots__ = ('c','prio','left','right','size')
    def __init__(self, c):
        self.c = c
        self.prio = random.randrange(1<<30)
        self.left = None
        self.right = None
        self.size = 1

def update(node):
    if node:
        node.size = 1
        if node.left:
            node.size += node.left.size
        if node.right:
            node.size += node.right.size

def split(root, k):
    if not root:
        return None, None

    left_size = root.left.size if root.left else 0
    if k <= left_size:
        l, r = split(root.left, k)
        root.left = r
        update(root)
        return l, root
    else:
        l, r = split(root.right, k - left_size - 1)
        root.right = l
        update(root)
        return root, r

def merge(left, right):
    if not left or not right:
        return left or right

    if left.prio > right.prio:
        left.right = merge(left.right, right)
        update(left)
        return left
    else:
        right.left = merge(left, right.left)
        update(right)
        return right

def build_treap(s):
    root = None
    for ch in s:
        node = Node(ch)
        root = merge(root, node)

    return root

def inorder(root, out):
    if not root:
        return

    inorder(root.left, out)
    out.append(root.c)
    inorder(root.right, out)

def start():
    s = input().rstrip('\n')
    q = int(input())
    root = build_treap(s)
    for _ in range(q):
        i, j, k = map(int, input().split())
        a, bc = split(root, i)
        b, c = split(bc, j - i + 1)
        root = merge(a, c)
        left, right = split(root, k)
        root = merge(merge(left, b), right)

    res = []
    inorder(root, res)
    sys.stdout.write(''.join(res))

start()
