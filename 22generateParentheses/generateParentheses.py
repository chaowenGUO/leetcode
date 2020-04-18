class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[''], *([] for _ in range(n))]
        for i in range(n + 1):
            for j in range(i): dp[i] += (f'({x}){y}' for x, y in itertools.product(dp[j], dp[i - j - 1]))
        return dp[-1]
