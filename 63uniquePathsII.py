class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int: 
        dp = [*itertools.accumulate((1 - _ for _ in obstacleGrid[0]), operator.mul)]
        for row in range(1, len(obstacleGrid)):
            dp[0] *= 1 - obstacleGrid[row][0]
            for column in range(1, len(obstacleGrid[0])): dp[column] = (dp[column - 1] + dp[column]) * (1 - obstacleGrid[row][column])
        return dp[-1]
