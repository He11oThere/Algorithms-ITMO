import sys

def read_data():
    data = sys.stdin.read().splitlines()
    n = int(data[0])
    cmds = [line.split() for line in data[1:1+n]]

    return cmds


def process(cmds):
    stack = []
    max_stack = []
    out = []
    for cmd in cmds:
        if cmd[0] == 'push':
            x = int(cmd[1])
            stack.append(x)
            if not max_stack or x > max_stack[-1]:
                max_stack.append(x)
            else:
                max_stack.append(max_stack[-1])
        elif cmd[0] == 'pop':
            if stack:
                stack.pop()
                max_stack.pop()
        else:
            if max_stack:
                out.append(str(max_stack[-1]))
    return out


cmds = read_data()
result = process(cmds)
print("\n".join(result))

