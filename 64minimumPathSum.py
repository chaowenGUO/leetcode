class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        column = len(grid[0])
        dp = [grid[0][0], *itertools.repeat(0, column - 1)]
        for _ in range(1, column): dp[_] = dp[_ - 1] + grid[0][_]
        for row in range(1, len(grid)):
            dp[0] += grid[row][0]
            for _ in range(1, column):
                dp[_] = min(dp[_], dp[_ - 1]) + grid[row][_]
        return dp[-1]
