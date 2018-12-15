class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 1 if n < 4 else 3**((n - 2) // 3) * ((n - 2) % 3 + 2)
