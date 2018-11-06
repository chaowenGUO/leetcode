class Solution:
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            _ = left**2 + right**2
            if _ == c: return True
            elif _ < c: left += 1
            else: right -= 1
        return False
