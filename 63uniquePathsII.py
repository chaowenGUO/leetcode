class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [0, 1] + [0] * (len(obstacleGrid[0]) - 1)
        for row in range(1, len(obstacleGrid) + 1):
            for column in range(1, len(obstacleGrid[0]) + 1): dp[column] = (not obstacleGrid[row - 1][column - 1]) * (dp[column - 1] + dp[column])
        return dp[-1]
