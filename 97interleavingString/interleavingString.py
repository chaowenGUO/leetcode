class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        else:
            dp = [True, *itertools.repeat(False, len(s2))]
            for column in range(1, len(dp)): dp[column] = dp[column - 1] and s3[column - 1] == s2[column - 1]
            for row in range(1, len(s1) + 1):
                dp[0] = dp[0] and s3[row - 1] == s1[row - 1]
                for column in range(1, len(dp)): dp[column] = dp[column] and s3[row + column - 1] == s1[row - 1] or dp[column - 1] and s3[row + column - 1] == s2[column - 1]
            return dp[-1]
    
    
