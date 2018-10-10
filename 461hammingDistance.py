class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        n = x ^ y
        result = 0
        while n:
            n &= n - 1
            result += 1
        return result
