class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num + 1)
        for _ in range(1, len(dp)): dp[_] = dp[_ >> 1] + (_ & 1)
        return dp
