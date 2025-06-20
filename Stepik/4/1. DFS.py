import sys

def read_data():
    data = sys.stdin.read().split()
    n = int(data[0])
    nodes = []
    i = 1

    for _ in range(n):
        val = int(data[i])
        l = int(data[i+1])
        r = int(data[i+2])
        nodes.append((val, l, r))
        i += 3

    return n, nodes

def build_tree(nodes): # (value, left_index, right_index)
    return nodes

def preorder(nodes, u, res):
    if u == -1:
        return

    val, l, r = nodes[u]
    res.append(str(val))
    preorder(nodes, l, res)
    preorder(nodes, r, res)

def inorder(nodes, u, res):
    if u == -1:
        return

    val, l, r = nodes[u]
    inorder(nodes, l, res)
    res.append(str(val))
    inorder(nodes, r, res)

def postorder(nodes, u, res):
    if u == -1:
        return

    val, l, r = nodes[u]
    postorder(nodes, l, res)
    postorder(nodes, r, res)
    res.append(str(val))

n, nodes = read_data()
root = 0
pre = []; inorder_res = []; post = []
preorder(nodes, root, pre)
inorder(nodes, root, inorder_res)
postorder(nodes, root, post)
print(" ".join(pre))
print(" ".join(inorder_res))
print(" ".join(post))
