class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 0, x // 2 + 1
        while left + 1 < right:
            middle = left + (right - left) // 2
            if middle**2 < x: left = middle
            else: right = middle
        return right if right**2 == x else left
