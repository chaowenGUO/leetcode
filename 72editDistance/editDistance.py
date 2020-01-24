class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        *dp, = range(len(word2) + 1)
        for row in range(1, len(word1) + 1):
            prev = [*dp]
            dp[0] = row
            for column in range(1, len(dp)): dp[column] = min(dp[column - 1] + 1, prev[column] + 1, prev[column - 1] + 1, prev[column - 1] if word1[row - 1] == word2[column - 1] else math.inf)
        return dp[-1]
