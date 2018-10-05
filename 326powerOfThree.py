class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()
