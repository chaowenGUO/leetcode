class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [True, *itertools.repeat(False, len(p))]
        for column in range(1, len(dp)):
            if p[column - 1] == '*': dp[column] = dp[column - 1]
        prev = dp[:]
        for row in range(1, len(s) + 1):
            dp[0] = False
            for column in range(1, len(dp)):
                if s[row - 1] == p[column - 1] or p[column - 1] == '?': dp[column] = prev[column - 1]
                elif p[column - 1] == '*': dp[column] = dp[column - 1] or prev[column]                   
                else: dp[column] = False
            prev, dp = dp, prev              
        return prev[-1]
