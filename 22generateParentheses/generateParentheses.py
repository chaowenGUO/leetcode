class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[''], *([] for _ in range(n))]
        for i in range(n + 1):
            for j in range(i):
                dp[i] += (f'({x}){y}' for ｘ in dp[j] for y in dp[i - j - 1])
        return dp[-1]
