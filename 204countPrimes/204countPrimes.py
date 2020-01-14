class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        else:
            result = [1] * n
            result[0] = result[1] = 0
            for _ in range(2, int(math.sqrt(n)) + 1): result[_**2::_] = itertools.repeat(0, len(result[_**2::_]))
            return sum(result)
