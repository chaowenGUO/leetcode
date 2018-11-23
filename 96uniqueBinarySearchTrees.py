class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        catalan = 1
        for _ in range(n): catalan = catalan * 2 * (2 * _ + 1) // (_ + 2)
        return catalan
