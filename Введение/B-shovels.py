def count_pairs(n: int) -> int:
    if 2 * n < 10:
        return 0

    base = 1
    while base * 10 <= 2 * n:
        base *= 10

    m = (2 * n - base) // base
    split = (n - base + 2) // base

    k = 0

    if split >= 0:
        lower = (base // 2) * (split * (split + 1) // 2)
        lower_extra = (split + 1) * ((base - 2) // 2)
        k += lower + lower_extra

    upper = max(split + 1, 0)
    if m >= upper:
        k_upper = m - upper + 1
        sum_upper = (upper + m) * k_upper // 2
        term_upper = k_upper * n
        term_subtract = (base // 2) * sum_upper
        term_fix = k_upper * ((base - 2) // 2)
        k += term_upper - term_subtract - term_fix

    return k

n = int(input())
print(count_pairs(n))
