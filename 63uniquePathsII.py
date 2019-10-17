class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        column = len(obstacleGrid[0])
        dp = [1 - obstacleGrid[0][0], *itertools.repeat(0, column - 1)]
        for _ in range(1, column): dp[_] = dp[_ - 1] * (1 - obstacleGrid[0][_])
        for row in range(1, len(obstacleGrid)):
            dp[0] *= 1 - obstacleGrid[row][0]
            for _ in range(1, column): dp[_] = (dp[_ - 1] + dp[_]) * (1 - obstacleGrid[row][_])
        return dp[-1]
