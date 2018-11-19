class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        if n < 2: return 0
        else:
            data = [1] * n
            data[0] = data[1] = 0
            for _ in range(2, int(math.sqrt(n)) + 1): data[_**2:n:_] = [0] * len(data[_**2:n:_])
            return sum(data)
