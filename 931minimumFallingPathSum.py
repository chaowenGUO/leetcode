class Solution:
    def minFallingPathSum(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        import functools
        return min(functools.reduce(lambda dp, row: [value + min(dp[column], dp[max(column - 1, 0)], dp[min(column + 1, len(A) - 1)]) for column, value in enumerate(row)], A))
