class Solution:
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for _ in range(2, n + 1):
            while n % _ == 0:
                result += _
                n //= _
        return result
