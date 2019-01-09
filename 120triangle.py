class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        import functools
        return functools.reduce(lambda dp, row: [value + min(dp[column], dp[column + 1]) for column, value in enumerate(row)], reversed(triangle))[0]
