class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        *dp, = itertools.accumulate(grid[0])
        for row in itertools.islice(grid, 1, None):
            dp[0] += row[0]
            for column in range(1, len(row)): dp[column] = min(itertools.islice(dp, column - 1, column + 1)) + row[column]
        return dp[-1]
