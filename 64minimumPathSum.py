class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [*itertools.accumulate(grid[0])]
        for row in range(1, len(grid)):
            dp[0] += grid[row][0]
            for column in range(1, len(grid[0])): dp[column] = min(dp[column], dp[column - 1]) + grid[row][column]
        return dp[-1]
