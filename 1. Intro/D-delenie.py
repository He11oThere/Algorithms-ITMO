import sys

def primes(n: int) -> list[int]:
    """
    возвращает массив всех простых делителей числа n. O(sqrt(n)) - оценка
    """

    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1 if d == 2 else 2

    if n > 1:
        factors.append(n)

    return factors

def count_factors(nums: list[int]) -> dict[int, int]:
    """
    суммарные простые множители для всего массива nums. \n
    m - размер nums,\n
    примерная оценка O(m*sqrt(n))
    """

    counts = {}
    for num in nums:
        if num != 1:
            prime_factors = primes(num)
            for i in prime_factors:
                counts[i] = counts.get(i, 0) + 1
    return counts

def is_equal(n: int, nums: list[int]) -> str:
    """
    проверка делимости количества всех вхождений каждого простого числа на n\n
    если делится, то yes, если нет - no \n
    такая же оценка как у предыдущего
    """

    counts = count_factors(nums)
    for i, count in counts.items():
        if count % n != 0:
            return "no"
    return "yes"

def main():
    """
    примерная оценка - O(t * m * sqrt(n)), где t - кол-во тестов
    """
    inp = sys.stdin.read().strip().split('\n')
    t = int(inp[0])
    i = 1

    for _ in range(t):
        n = int(inp[i])
        i += 1

        nums_line = inp[i].split()
        i += 1

        nums = list(map(int, nums_line))

        print(is_equal(n, nums))

main()
