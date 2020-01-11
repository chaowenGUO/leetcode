class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        *dp, = itertools.accumulate((1 - _ for _ in obstacleGrid[0]), operator.mul)
        for row in itertools.islice(obstacleGrid, 1, None):
            dp[0] *= 1 - row[0]
            for column in range(1, len(row)): dp[column] = sum(itertools.islice(dp, column - 1, column + 1)) * (1 - row[column])
        return dp[-1]
