class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[_ + 1] - prices[_]) for _ in range(len(prices) - 1))
