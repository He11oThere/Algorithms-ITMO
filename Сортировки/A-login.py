def recursion(first_part: str, surname: str, f_l: str):
    if not first_part:
        return f_l + surname[0]

    first_letter = first_part[0]

    if first_letter < surname[0]:
        return recursion(first_part[1:], surname, f_l + first_letter)
    else:
        return f_l + surname[0]

def login(inp: list[str]):
    name = inp[0]
    surname = inp[1]
    first_letter = name[0]
    return recursion(name[1:], surname, first_letter)

inp = input().strip().split()
print(login(inp))
