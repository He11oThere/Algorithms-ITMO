def is_possible(eq: str):
    left, right = eq.replace(" ", "").split('=')
    n = int(right)
    questions_count = left.count('?')
    pluses_count = left.count("+") + 1
    minuses_count = left.count("-")

    min_s = 1 * pluses_count - n * minuses_count
    max_s = n * pluses_count - 1 * minuses_count

    if not(min_s <= n <= max_s):
        print("Impossible")
        return

    if questions_count == 0: print("Impossible"); return

    parts = eq.split()[:-2]

    signs = []
    questions_indexes = []
    curr_sign = +1

    for i, j in enumerate(parts):
        if j == "?":
            signs.append(curr_sign)
            questions_indexes.append(i)
        elif j == "+": curr_sign = +1
        else: curr_sign = -1

    min_suf: list = [0] * (questions_count + 1)
    max_suf: list = [0] * (questions_count + 1)

    for i in range(questions_count-1, -1, -1):
        if signs[i] == +1:
            min_suf[i] = min_suf[i+1] + 1
            max_suf[i] = max_suf[i+1] + n
        else:
            min_suf[i] = min_suf[i+1] - n
            max_suf[i] = max_suf[i+1] - 1


    partial_sum = 0
    ans = [0] * questions_count

    for i in range(questions_count):
        sign = signs[i]

        if sign == +1:
            lower_bound = (n - partial_sum) - max_suf[i + 1]
            upper_bound = (n - partial_sum) - min_suf[i + 1]
        else:
            lower_bound = (partial_sum - n) + min_suf[i + 1]
            upper_bound = (partial_sum - n) + max_suf[i + 1]

        ans_low = max(lower_bound, 1)
        ans_high = min(upper_bound, n)

        if ans_low > ans_high:
            print("Impossible")
            return

        elem_i = ans_low
        ans[i] = elem_i
        partial_sum += sign * elem_i

    # finally
    print("Possible")

    ans_ind = 0
    p = []
    curr_sign = +1
    for i in parts:
        if i == "?":
            p.append(str(ans[ans_ind]))
            ans_ind += 1
        else: p.append(i)

    left_expr = " ".join(p)
    print(f"{left_expr} = {n}")

    # print(left)
    # print(n)
    # print(signs)
    # print(questions_indexes)

# is_possible("? + ? - ? + ? + ? = 42")
inp = input()
is_possible(inp)