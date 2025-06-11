def check_brackets(s):
    stack = []
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for i, char in enumerate(s):
        if char in "([{":
            stack.append((char, i + 1))
        elif char in ")]}":
            if not stack or stack[-1][0] != bracket_pairs[char]:
                return i + 1
            stack.pop()

    return "Success" if not stack else stack[0][1]

s = input().strip()
print(check_brackets(s))
