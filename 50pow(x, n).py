class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: x, n = 1 / x, -n
        result = 1
        while n:
            if n & 1: result *= x
            x *= x
            n >>= 1
        return result
