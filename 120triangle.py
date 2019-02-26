import functools

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return functools.reduce(lambda dp, row: [value + min(dp[column], dp[column + 1]) for column, value in enumerate(row)], reversed(triangle))[0]
