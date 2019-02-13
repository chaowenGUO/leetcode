import typing
class Solution:
    def minFallingPathSum(self, A: typing.List[typing.List[int]]) -> int:
        import functools
        return min(functools.reduce(lambda dp, row: [value + min(dp[max(0, column - 1)], dp[column], dp[min(column + 1, len(A) - 1)]) for column, value in enumerate(row)], A))
