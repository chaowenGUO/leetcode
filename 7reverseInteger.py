class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = (x > 0) - (x < 0)
        x = abs(x)
        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return sign * result if result < 2**31 else 0
