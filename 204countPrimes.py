class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        else:
            data = [1] * n
            data[0] = data[1] = 0
            for _ in range(2, int(math.sqrt(n)) + 1): data[_**2::_] = itertools.repeat(0, len(data[_**2::_]))
            return sum(data)
